var app = angular.module("app", [
  "app.factory.auth",
  "app.factory.user",
  "app.factory.trade",
  "app.auth",
  "app.info",
  "ngRoute",
  "ngMessages"
]).config(["$routeProvider", function($routeProvider){
  $routeProvider.when("/", {
    templateUrl: "static/info/info.html",
    controller: "InfoController"
  }).when("/signin", {
    templateUrl: "static/auth/signin.html",
    controller: "AuthController"
  }).when("/signup", {
    templateUrl: "static/auth/signup.html",
    controller: "AuthController"
  }).otherwise({
    redirectTo: "/"
  });
}]).factory("AttachTokens", function($window){
  var attach = {
    request: function(obj){
      var jwt = $window.localStorage.getItem("com.app");
      if(jwt){
        obj.headers["x-access-token"] = jwt;
      }
      obj.headers["Allow-Control-Allow-Origin"] = "*";
      return obj;
    }
  };
}).run(function($rootScope, $location, Auth){
  $rootScope.$on("$routeChangeStart", function(evt, next, current){
    if (next.$$route && next.$$route.authenticate && !Auth.isAuth()) {
      $location.path("/signin");
    }
  })
})
