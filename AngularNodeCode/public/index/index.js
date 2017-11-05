angular.module('myApp', [
  'ngRoute',
  'home',
  'signIn'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/home'});
}]);