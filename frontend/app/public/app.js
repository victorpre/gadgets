'use strict';

var ajax = angular.module("ajax", []);
var navbar = angular.module("navbar", []);

var gadgets = angular.module("gadgets", [
        'ngResource'
    ]);

angular
    .module('GadgetsApp', [
      'appRoutes',
      'ngMaterial',
      'md.data.table',
      'ajax',
      'navbar',
      'gadgets'
    ]);
