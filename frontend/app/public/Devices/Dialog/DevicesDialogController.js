dialog.controller('DevicesDialogController', DevicesDialogController );

function DevicesDialogController($scope, device, DevicesDialogService) {
  $scope.dialogService = DevicesDialogService;
  $scope.device = angular.copy(device);
}
