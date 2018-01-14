gadgets.factory('GadgetsService', GadgetsService);

function GadgetsService($q, $filter, Ajax) {

  var devicesEndpoint = 'api/devices/';
  var deviceModelsEndpoint = 'api/device_models/';

  var service = {
    init: init,
    getDeviceModelName: getDeviceModelName,
    addDevice: addDevice
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
    // SEND to backend
    console.log(device);
  }
};
