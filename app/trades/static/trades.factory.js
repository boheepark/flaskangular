angular.module("app.factory.trades", []).factory("Trade", function ($http, $location, $window) {
  var buy = function(req){
    return $http({
      method: "POST",
      url: "/api/trades/buy",
      data: req
    }).then(function(res){
      return res.data;
    });
  };
  return {
    buy: buy
  };
});
