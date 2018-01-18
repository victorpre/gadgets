dialog.factory('DialogService', DialogService);

function DialogService($mdDialog, DevicesService) {
  var service = {
    openAddDeviceDialog: openAddDeviceDialog,
    cancel: cancel,
    addDevice: addDevice,
    getDeviceModelOptions: getDeviceModelOptions,
    isCreate: false
  };


  return service;

  function openAddDeviceDialog(device, index){
    if (typeof device !== "undefined") {
      service.editedAt = index;
      service.isCreate = false;
    } else {
      service.isCreate = true;
    }

    $mdDialog.show({
      controller: DialogController,
      templateUrl: 'public/Devices/_add_dialog.html',
      parent: angular.element(document.body),
      clickOutsideToClose: true,
      locals: {
        device: device
      },
      fullscreen: true
    });
  }

  function cancel(){
    $mdDialog.cancel();
    service.editableDevice = {};
  }

  function addDevice(device) {
    if (service.isCreate) {
      DevicesService.addDevice(device);
    } else{
      DevicesService.editDevice(device, service.editedAt);
    }
    cancel();
  }

  function getDeviceModelOptions() {
    return DevicesService.device_models;
  }
}
