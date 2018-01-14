devices.controller('DevicesController', DevicesController );

function DevicesController($scope, DialogService, DevicesService) {
  $scope.selected = [];
  $scope.query = {
    order: 'id',
    limit: 5,
    page: 1
  };

  $scope.service = DevicesService;
  $scope.service.init();

  $scope.dialogService = DialogService;

}
