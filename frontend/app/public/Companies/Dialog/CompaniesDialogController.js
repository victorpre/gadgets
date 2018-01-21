dialog.controller('CompaniesDialogController', CompaniesDialogController );

function CompaniesDialogController($scope, company, CompaniesDialogService) {
  $scope.dialogService = CompaniesDialogService;
  $scope.company = angular.copy(company);
}
