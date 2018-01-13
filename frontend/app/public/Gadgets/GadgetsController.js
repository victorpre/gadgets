gadgets.controller('GadgetsController', GadgetsController );

function GadgetsController($scope, GadgetsService) {
  $scope.selected = [];
  $scope.query = {
    order: 'name',
    limit: 5,
    page: 1
  };

  $scope.service = GadgetsService;
  $scope.service.init();
}
