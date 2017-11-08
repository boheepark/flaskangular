angular.module("app.factory.trade", []).factory("Trade", function ($http, $location, $window) {
  var buy = function(req){
    return $http({
      method: "POST",
      url: "/api/trade/buy",
      data: req
    }).then(function(res){
      return res.data;
    });
  };
  return {
    buy: buy
  };
});
