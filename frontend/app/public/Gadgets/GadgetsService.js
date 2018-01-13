gadgets.factory('GadgetsService', GadgetsService);

function GadgetsService(Ajax) {

  var projectsApiBulkEndpoint = 'api/devices/';

  var service = {
    init: init
  };

  return service;

  function init() {
    service.devices = [];
    var promisse = Ajax.get(projectsApiBulkEndpoint);
    promisse.then(function(result){
      console.log(result);
      service.devices = result.data;
    });
    return promisse;
  }
};
