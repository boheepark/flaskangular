angular.module("app.auth").directive('checkDb', ['Auth', function(Auth) {
  return {
    require: 'ngModel',
    link: function($scope, $element, $attrs, ngModel) {
      var db = $attrs.checkDb;
      function setAsLoading(bool) {
        ngModel.$setValidity('recordLoading', !bool);
      }
      function setAsAvailable(bool) {
        ngModel.$setValidity('recordAvailable', bool);
      }
      ngModel.$parsers.push(function(value) {
        if (!value || value.length == 0) return;
        setAsLoading(true);
        setAsAvailable(false);
        Auth.isUnique(db, { "value": value }).then(function(data){
          if(data.value){
            setAsLoading(false);
            setAsAvailable(true);
          } else if(!data.value){
            setAsLoading(false);
            setAsAvailable(false);
          }
        });
        return value;
      })
    }
  }
}]);
