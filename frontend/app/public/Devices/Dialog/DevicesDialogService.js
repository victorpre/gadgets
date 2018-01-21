dialog.factory('DevicesDialogService', DevicesDialogService);

function DevicesDialogService($mdDialog, DevicesService) {
  var service = {
    openAddDeviceDialog: openAddDeviceDialog,
    addDevice: addDevice,
    cancel: cancel,
    getDeviceModelOptions: getDeviceModelOptions,
    isCreate: false
  };


  return service;

  function cancel(){
    $mdDialog.cancel();
    service.editableDevice = {};
  }

  function getDeviceModelOptions() {
    return DevicesService.device_models;
  }

  // Devices
  function openAddDeviceDialog(device, index){
    if (typeof device !== "undefined") {
      service.editedAt = index;
      service.isCreate = false;
    } else {
      service.isCreate = true;
    }

    $mdDialog.show({
      controller: DevicesDialogController,
      templateUrl: 'public/Devices/_add_dialog.html',
      parent: angular.element(document.body),
      clickOutsideToClose: true,
      locals: {
        device: device
      },
      fullscreen: true
    });
  }

  function addDevice(device) {
    if (service.isCreate) {
      DevicesService.addDevice(device);
    } else{
      DevicesService.editDevice(device, service.editedAt);
    }
    cancel();
  }
}
