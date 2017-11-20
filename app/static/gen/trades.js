angular.module("app.factory.trades",[]).factory("Trade",function($http,$location,$window){var buy=function(req){return $http({method:"POST",url:"/api/trades/buy",data:req}).then(function(res){return res.data;});};return{buy:buy};});angular.module('app.home').directive("trades",["$timeout","Trade",function($timeout,Trade){return{templateUrl:"templates/trades/trades.html",link:function($scope,$element,$attrs,ngModel){$scope.buy=function(){if(!$scope.stock.company||!$scope.stock.price||!$scope.stock.quantity){$scope.error.message="The following are required:";if(!$scope.stock.company)$scope.error.message+=" Company";if(!$scope.stock.price)$scope.error.message+=" Price";if(!$scope.stock.quantity)$scope.error.message+=" Quantity";$scope.error.shown=true;}else if($scope.user.trading>=$scope.stock.total){$scope.error.shown=false;Trade.buy($scope.stock).then(function(res){$scope.user=res.data.user;$scope.trades=res.data.trades;}).catch(function(error){console.log(error);});}else{$scope.error.message="Insufficient Trading Balance. You need to deposit at least $"+($scope.stock.total-Number($scope.user.trading));$scope.error.shown=true;}};$scope.onPress=function(event){if(event.keyCode===13)$scope.buy();};$scope.sortType="name";$scope.sortReverse=false;$scope.search="";$scope.error={"shown":false,"message":""};}};}]);