devices.controller('DevicesController', DevicesController );

function DevicesController($scope, DevicesDialogService, DevicesService) {
  $scope.query = {
    order: 'id',
    limit: 5,
    page: 1
  };

  $scope.service = DevicesService;
  $scope.service.init();

  $scope.dialogService = DevicesDialogService;

  $scope.filters_partial = 'public/Devices/_filters.html'
}
