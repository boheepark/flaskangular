angular.module("app.auth").directive("checkPw", ["$timeout", function($timeout){
  return {
    restrict: "A",
    require: "ngModel",
    link: function($scope, $element, $attrs, ngModel){
      ngModel.$validators.checkPw = function(modelValue){
        var has = function(string){
          var bool = false;
          for(var c of string){
            if(modelValue.includes(c)) bool = true;
          }
          return bool;
        }
        if(!has("abcdefghijklmnopqrstuvwxyz") || !has("ABCDEFGHIJKLMNOPQRSTUVWXYZ") || !has("123456789") || !has("~!@#$%^&*()_+-=/?<>:;{}[]|")) return false;
        return true;
      };
    }
  }
}]);
