dialog.controller('DialogController', DialogController );

function DialogController($scope, $mdDialog, GadgetsService) {
  $scope.service = GadgetsService;
  $scope.service.init();

  $scope.hide = function() {
    $mdDialog.hide();
  };

  $scope.cancel = function() {
    $mdDialog.cancel();
  };

  $scope.addDevice = function(device) {
    $scope.service.addDevice(device);
    $mdDialog.hide();
  };
}
