'use strict';

angular.module('addArticle', ['ngRoute','myAppService'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/addArticle', {
    templateUrl: '../addArticle/addArticle.html',
    controller: 'AddArticleCtrl'
  });
}])

.controller('AddArticleCtrl', ['$scope','CommonProp','$http','$location',function($scope,CommonProp,$http,$location) {
	$scope.addArticle = function(title, content, category){
		
        var auth = CommonProp.getUserAuth();
	
        var user = CommonProp.getUser();

	$http.defaults.headers.common = {"Access-Control-Request-Headers": "accept, origin, authorization"};
    	$http.defaults.headers.common = {"Access-Control-Expose-Headers": "Origin, X-Requested-With, Content-Type, Accept"};
	$http.defaults.headers.common["Cache-Control"] = "no-cache";
    	$http.defaults.headers.common.Pragma = "no-cache";
    	$http.defaults.headers.common['Authorization'] = 'Basic '+auth;
    
	$http({method: 'POST',cache: false, url: 'http://127.0.0.1:5000/article',data: { name: title, content: content, category : {catName : category}, uid: {username : user}} }).
            success(function(data, status, headers, config) {
		$location.path('/userHome');
            }).
            error(function(data, status, headers, config) {
                console.log(data,status);
            });	
	
	};
}]);
