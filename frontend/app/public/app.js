'use strict';

var ajax = angular.module("ajax", []);

var gadgets = angular.module("gadgets", [
        'ngResource'
    ]);

angular
    .module('GadgetsApp', [
      'appRoutes',
      'ngMaterial',
      'ajax',
      'gadgets'
    ]);
