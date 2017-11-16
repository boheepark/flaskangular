angular.module('app.info', []).controller('InfoController', function ($scope, $rootScope, $window, $location, Auth, User, Trade) {
  $scope.signout = function(){
    Auth.signout();
  };
  var token = $window.localStorage.getItem("com.app");
  $scope.getUserByToken = function(){
    User.getUserByToken(token).then(function(res){
      if(res.status === "fail"){
        Auth.signout();
      } else {
        $scope.user = res.data;
        $scope.user.sum = Number($scope.user.checking) + Number($scope.user.trading);
        $scope.stock = {
          "user_id": $scope.user.id,
          "price": 0.0,
          "quantity": 0,
          "total": 0.0,
          "date": new Date()
        };
      }
      }).catch(function(e) {
        console.log(e);
      });
  };
  $scope.getTradesByToken = function(){
    User.getTradesByToken(token).then(function(res){
      if(res.status === "fail"){
        Auth.signout();
      } else {
        $scope.trades = res.data;
      }
      }).catch(function(e) {
        console.log(e);
      });
  };
  if(token){
    $scope.getUserByToken();
    $scope.getTradesByToken();
  } else {
    $scope.signout();
  }
  $scope.updateTotalStockPrice = function(){
     $scope.stock.total = $scope.stock.price * $scope.stock.quantity;
  };
});
