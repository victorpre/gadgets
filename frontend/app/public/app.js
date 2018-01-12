'use strict';

var retail = angular.module("retail", [
        'ngResource'
    ]);

var gadgets = angular.module("gadgets", [
        'ngResource'
    ]);

angular
    .module('GadgetsApp', [
        'appRoutes',
        'ngMaterial',
        'gadgets'
    ]);
