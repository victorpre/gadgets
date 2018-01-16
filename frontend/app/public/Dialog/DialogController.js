dialog.controller('DialogController', DialogController );

function DialogController($scope, DialogService) {
  $scope.dialogService = DialogService;
  $scope.device = $scope.dialogService.editableDevice;
}
