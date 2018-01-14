devices.factory('DevicesService', DevicesService);

function DevicesService($q, $filter, Ajax) {

  var devicesEndpoint = 'api/devices/';
  var deviceModelsEndpoint = 'api/device_models/';

  var service = {
    init: init,
    getDeviceModelName: getDeviceModelName,
    addDevice: addDevice,
    getDeviceModelOptions: getDeviceModelOptions
  };

  return service;

  function init() {
    var defer = $q.defer();
    service.devices = [];
    service.device_models = [];
    var promisses = {};
    promisses.devices = Ajax.get(devicesEndpoint);
    promisses.device_models = Ajax.get(deviceModelsEndpoint);
    $q.all(promisses).then(function(result) {
      console.log(result);
      service.devices = result.devices.data;
      service.device_models = result.device_models.data;
    }, function(error){
      defer.reject(error);
    });
    return defer.promise;
  }

  function getDeviceModelName(id) {
    return $filter('filter')(service.device_models, {'id': id})[0].name;
  }

  function addDevice(device) {
    var promisse;
    promisse = Ajax.post(devicesEndpoint, device);
    promisse.then(success, error);
    return promisse;

    function success(result) {
      console.log(result);
      service.devices.push(result.data);
    }

    function error(result) {
      console.log(result);
    }
  }

  function getDeviceModelOptions() {
    var defer = $q.defer();
    var promisses = {};
    promisses.device_models = Ajax.get(deviceModelsEndpoint);
    $q.all(promisses).then(function(result) {
      service.device_models = result.device_models.data;
      console.log("oie");
    }, function(error){
      defer.reject(error);
    });
    return defer.promise;
  }
};
