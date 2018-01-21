companies.controller('CompaniesController', CompaniesController );

function CompaniesController($scope, CompaniesDialogService, CompaniesService) {
 $scope.query = {
    order: 'id',
    limit: 5,
    page: 1
  };

  $scope.service = CompaniesService;
  $scope.service.init();

  $scope.dialogService = CompaniesDialogService;
}
