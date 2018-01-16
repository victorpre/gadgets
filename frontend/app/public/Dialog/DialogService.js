dialog.factory('DialogService', DialogService);

function DialogService($mdDialog, DevicesService) {
  var service = {
    openAddDeviceDialog: openAddDeviceDialog,
    cancel: cancel,
    addDevice: addDevice,
    getDeviceModelOptions: getDeviceModelOptions,
    editableDevice: {},
    isCreate: false
  };


  return service;

  function openAddDeviceDialog(device){
    if (typeof device !== "undefined") {
      service.editableDevice = device;
      service.isCreate = false;
    } else {
      service.isCreate = true;
    }

    $mdDialog.show({
      controller: DialogController,
      templateUrl: 'public/Devices/_add_dialog.html',
      parent: angular.element(document.body),
      clickOutsideToClose: true,
      // refactor
      onRemoving: function(el, rm){
        service.editableDevice = {};
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
      console.log("TODO: send to backend");
    }
    cancel();
  }

  function getDeviceModelOptions() {
    return DevicesService.device_models;
  }
}
