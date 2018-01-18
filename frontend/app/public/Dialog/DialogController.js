dialog.controller('DialogController', DialogController );

function DialogController($scope, device, DialogService) {
  $scope.dialogService = DialogService;
  $scope.device = angular.copy(device);
}
