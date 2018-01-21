'use strict';

var ajax = angular.module("ajax", []);
var navbar = angular.module("navbar", []);
var dialog = angular.module("dialog", []);

var devices = angular.module("devices", [
        'ngResource'
    ]);

var companies = angular.module("companies", [
        'ngResource'
    ]);

angular
    .module('GadgetsApp', [
      'appRoutes',
      'ngMaterial',
      'md.data.table',
      'ajax',
      'navbar',
      'dialog',
      'devices',
      'companies'
    ]);
