angular.module("app.auth", []).controller('AuthController', function($scope, $timeout, $window, $location, Auth){
  $scope.signin = function(user){
    Auth.signin(user).then(function(data){
      $location.path('/');
    }).catch(function (error) {
      console.log(error);
    });
  };
  $scope.signup = function(user){
    Auth.signup(user).then(function(data){
      $location.path('/');
    }).catch(function (error) {
      console.log(error);
    });
  };
  $scope.setupLabels = function(){
    var labels = document.querySelectorAll(".auth-input__label-text");
    var inputs = document.querySelectorAll(".auth-input__input");
    labels.forEach(function(el){
      var text = el.innerText;
      var html = "";
      for(var l of text){
        if(l === " ") l = "&nbsp;";
        html += `<span class="letter">${l}</span>`;
      }
      el.innerHTML = html;
    });
    inputs.forEach(function(el){
      var parent = el.parentNode;
      el.addEventListener("focus", function(){
        parent.classList.add("filled");
        labelAnimationIn(parent, true);
      }, false);
      el.addEventListener("blur", function(){
        if(el.value.length) return;
        parent.classList.remove("filled");
        labelAnimationIn(parent, false);
      }, false);
    });
    function labelAnimationIn(parent, isFilled) {
      var act = (isFilled) ? "add" : "remove";
      var letters = parent.querySelectorAll(".letter");
      letters = [].slice.call(letters, 0);
      if (!isFilled) letters = letters.reverse();
      letters.forEach(function(el, i) {
        $timeout(function() {
          var contains = parent.classList.contains("filled");
          if ((isFilled && !contains) || (!isFilled && contains)) return;
          el.classList[act]("active");
        }, (50*i));
      });
    };
  };
  $scope.setupLoading = function(){
    $timeout(function(){
      var forms = document.getElementsByClassName("form-auth");
      for(var form of forms){
        form.classList.add("on-start");
      }
    }, 100);
    $timeout(function(){
      var forms = document.getElementsByClassName("form-auth");
      for(var form of forms){
        form.classList.add("document-loaded");
      }
    }, 1800);
  };
  $scope.setupLabels();
  $scope.setupLoading();
});
