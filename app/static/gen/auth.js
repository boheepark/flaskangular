angular.module("app.factory.auth",[]).factory("Auth",function($http,$location,$window,$timeout,$q){var signin=function(req){return $http({method:"POST",url:"/auth/signin",data:req}).then(function(res){$window.localStorage.setItem("com.app",res.data.token);return res.data;});};var signup=function(req){return $http({method:"POST",url:"/auth/signup",data:req}).then(function(res){$window.localStorage.setItem("com.app",res.data.token);return res.data;});};var isAuth=function(){return!!$window.localStorage.getItem("com.app");};var signout=function(){$window.localStorage.removeItem("com.app");$location.path("/signin");};var isUnique=function(db,value){if(db==="uname"){return $http({method:"POST",url:"/auth/checkUname",data:value}).then(function(res){return res.data;});}else if(db==="email"){return $http({method:"POST",url:"/auth/checkEmail",data:value}).then(function(res){return res.data;});}}
return{signin:signin,signup:signup,isAuth:isAuth,signout:signout,isUnique:isUnique};});angular.module("app.auth",[]).controller('AuthController',function($scope,$timeout,$window,$location,Auth){$scope.signin=function(user){Auth.signin(user).then(function(data){$location.path('/');}).catch(function(error){console.log(error);});};$scope.signup=function(user){Auth.signup(user).then(function(data){$location.path('/');}).catch(function(error){console.log(error);});};$scope.setupLabels=function(){var labels=document.querySelectorAll(".auth-input__label-text");var inputs=document.querySelectorAll(".auth-input__input");labels.forEach(function(el){var text=el.innerText;var html="";for(var l of text){if(l===" ")l="&nbsp;";html+=`<span class="letter">${l}</span>`;}
el.innerHTML=html;});inputs.forEach(function(el){var parent=el.parentNode;el.addEventListener("focus",function(){parent.classList.add("filled");labelAnimationIn(parent,true);},false);el.addEventListener("blur",function(){if(el.value.length)return;parent.classList.remove("filled");labelAnimationIn(parent,false);},false);});function labelAnimationIn(parent,isFilled){var act=(isFilled)?"add":"remove";var letters=parent.querySelectorAll(".letter");letters=[].slice.call(letters,0);if(!isFilled)letters=letters.reverse();letters.forEach(function(el,i){$timeout(function(){var contains=parent.classList.contains("filled");if((isFilled&&!contains)||(!isFilled&&contains))return;el.classList[act]("active");},(50*i));});};};$scope.setupLoading=function(){$timeout(function(){var forms=document.getElementsByClassName("form-auth");for(var form of forms){form.classList.add("on-start");}},100);$timeout(function(){var forms=document.getElementsByClassName("form-auth");for(var form of forms){form.classList.add("document-loaded");}},1800);};$scope.setupLabels();$scope.setupLoading();});angular.module("app.auth").directive("authBtn",["$timeout",function($timeout){return{templateUrl:"templates/auth/authBtn.html",link:function($scope,$element,$attrs){$scope.btn_text=$attrs.text;$scope.authorize=function(user){if($scope.btn_text==="Signup")$scope.signup(user);else if($scope.btn_text==="Signin")$scope.signin(user);};}}}]);angular.module("app.auth").component("bgEffect",{templateUrl:"templates/auth/bgEffect.html"});angular.module("app.auth").directive('checkDb',['Auth',function(Auth){return{require:'ngModel',link:function($scope,$element,$attrs,ngModel){var db=$attrs.checkDb;function setAsLoading(bool){ngModel.$setValidity('recordLoading',!bool);}
function setAsAvailable(bool){ngModel.$setValidity('recordAvailable',bool);}
ngModel.$parsers.push(function(value){if(!value||value.length==0)return;setAsLoading(true);setAsAvailable(false);Auth.isUnique(db,{"value":value}).then(function(data){if(data.value){setAsLoading(false);setAsAvailable(true);}else if(!data.value){setAsLoading(false);setAsAvailable(false);}});return value;})}}}]);angular.module("app.auth").directive("checkPw",["$timeout",function($timeout){return{restrict:"A",require:"ngModel",link:function($scope,$element,$attrs,ngModel){ngModel.$validators.checkPw=function(modelValue){var has=function(string){var bool=false;for(var c of string){if(modelValue.includes(c))bool=true;}
return bool;};if(!has("abcdefghijklmnopqrstuvwxyz")||!has("ABCDEFGHIJKLMNOPQRSTUVWXYZ")||!has("123456789")||!has("~!@#$%^&*()_+-=/?<>:;{}[]|"))return false;return true;};}};}]);angular.module("app.auth").directive("compareTo",["$timeout",function($timeout){return{require:"ngModel",scope:{otherModelValue:"=compareTo"},link:function($scope,$element,$attrs,ngModel){ngModel.$validators.compareTo=function(modelValue){return modelValue===$scope.otherModelValue;};$scope.$watch("otherModelValue",function(){ngModel.$validate();});}}}]);