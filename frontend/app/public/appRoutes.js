angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider','$locationProvider', '$urlRouterProvider', function($stateProvider, $locationProvider, $urlRouterProvider) {

      $stateProvider
        .state('devices',{
          url: '/',
          templateUrl: 'public/Devices/_devices.html',
          controller: 'DevicesController'
        })
        .state('companies',{
          url: '/companies',
          templateUrl: 'public/Companies/_companies.html',
          controller: 'CompaniesController'
        });

    $urlRouterProvider.otherwise('/');
}]);
