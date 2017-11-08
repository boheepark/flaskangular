angular.module("app.auth").directive("compareTo", ["$timeout", function($timeout){
  return {
    require: "ngModel",
    scope: {
      otherModelValue: "=compareTo"
    },
    link: function($scope, $element, $attrs, ngModel){
      ngModel.$validators.compareTo = function(modelValue){
        return modelValue === $scope.otherModelValue;
      };
      $scope.$watch("otherModelValue", function(){
        ngModel.$validate();
      });
    }
  }
}]);
