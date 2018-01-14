angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
    $stateProvider.state({
        name: 'devices',
        url: '/',
        templateUrl: 'public/Devices/_devices.html',
        controller: 'DevicesController'
    });

    $urlRouterProvider.otherwise('/');
}]);
