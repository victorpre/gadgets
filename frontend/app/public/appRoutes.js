angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
    $stateProvider.state({
        name: 'gadgets',
        url: '/',
        templateUrl: 'public/Gadgets/_gadgets.html',
        controller: 'GadgetsController'
    });

    $urlRouterProvider.otherwise('/');
}]);
