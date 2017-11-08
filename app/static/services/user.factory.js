angular.module("app.factory.user", []).factory("User", function ($http, $location, $window) {
  var getUserByToken = function(){
    return $http({
      method: "POST",
      url: "/api/user",
      data: { token: $window.localStorage.getItem("com.app") }
    }).then(function (res) {
      return res.data;
    });
  };
  var getTradesByToken = function() {
    return $http({
      method: 'POST',
      url: '/api/user/trades',
      data: { token: $window.localStorage.getItem('com.app') }
    }).then(function(res){
      return res.data;
    });
  };
  var getUsernames = function(){
    return $http({
      method: "GET",
      url: "/api/user/unames",
    }).then(function(res){
      return res.data;
    });
  };
  var getEmails = function(){
    return $http({
      method: "GET",
      url: "/api/user/emails",
    }).then(function(res){
      return res.data;
    });
  };
  return {
    getUserByToken: getUserByToken,
    getTradesByToken: getTradesByToken,
    getUsernames: getUsernames,
    getEmails: getEmails
  };
});
