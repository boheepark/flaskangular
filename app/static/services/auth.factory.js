angular.module("app.factory.auth", []).factory("Auth", function ($http, $location, $window, $timeout, $q) {
  var signin = function(req){
    return $http({
      method: "POST",
      url: "/auth/signin",
      data: req
    }).then(function(res){
      $window.localStorage.setItem("com.app", res.data.token);
      return res.data;
    });
  };
  var signup = function(req){
    return $http({
      method: "POST",
      url: "/auth/signup",
      data: req
    }).then(function(res){
      $window.localStorage.setItem("com.app", res.data.token);
      return res.data;
    });
  };
  var isAuth = function(){
    return !!$window.localStorage.getItem("com.app");  //ORG
  };
  var signout = function(){
    $window.localStorage.removeItem("com.app");
    $location.path("/signin");
  };
  var isUnique = function(db, value){
    if(db === "uname"){
      return $http({
        method: "POST",
        url: "/auth/checkUname",
        data: value
      }).then(function(res){
        return res.data;
      });
    } else if(db === "email"){
      return $http({
        method: "POST",
        url: "/auth/checkEmail",
        data: value
      }).then(function(res){
        return res.data;
      });
    }
  }
  return {
    signin: signin,
    signup: signup,
    isAuth: isAuth,
    signout: signout,
    isUnique: isUnique
  };
});
