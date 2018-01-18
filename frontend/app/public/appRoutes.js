angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider','$locationProvider', '$urlRouterProvider', function($stateProvider, $locationProvider, $urlRouterProvider) {

      $stateProvider
        .state('devices',{
          url: '/',
          templateUrl: 'public/Devices/_devices.html',
          controller: 'DevicesController'
        });

    $urlRouterProvider.otherwise('/');
    $locationProvider.html5Mode(true).hashPrefix('!');

}]);
