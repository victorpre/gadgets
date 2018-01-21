angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider','$locationProvider', '$urlRouterProvider', function($stateProvider, $locationProvider, $urlRouterProvider) {

      $stateProvider
        .state('Devices',{
          url: '/',
          templateUrl: 'public/Devices/_devices.html',
          controller: 'DevicesController'
        })
        .state('Companies',{
          url: '/companies',
          templateUrl: 'public/Companies/_companies.html',
          controller: 'CompaniesController'
        });

    $urlRouterProvider.otherwise('/');
    $locationProvider.html5Mode(true).hashPrefix('!');

}]);
