angular.module("app.auth").directive("authBtn", ["$timeout", function($timeout){
  return {
    templateUrl: "static/auth/authBtn.html",
    link: function($scope, $element, $attrs){
      $scope.btn_text = $attrs.text;
      $scope.authorize = function(user){
        if($scope.btn_text === "Signup") $scope.signup(user);
        else if($scope.btn_text === "Signin") $scope.signin(user);
      };
    }
  }
}]);
