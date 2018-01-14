dialog.factory('DialogService', DialogService);

function DialogService($mdDialog, DevicesService) {
  var service = {
    openAddDeviceDialog: openAddDeviceDialog,
    cancel: cancel,
    addDevice: addDevice,
    getDeviceModelOptions: getDeviceModelOptions
  };

  return service;

  function openAddDeviceDialog(ev){
    $mdDialog.show({
      controller: DialogController,
      templateUrl: 'public/Devices/_add_dialog.html',
      parent: angular.element(document.body),
      targetEvent: ev,
      clickOutsideToClose: true,
      fullscreen: true
    });
  }

  function cancel(){
    $mdDialog.cancel();
  }

  function addDevice(device) {
    DevicesService.addDevice(device)
    $mdDialog.hide();
  }

  function getDeviceModelOptions() {
    return DevicesService.device_models;
  }
}
