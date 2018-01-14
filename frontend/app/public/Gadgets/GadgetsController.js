gadgets.controller('GadgetsController', GadgetsController );

function GadgetsController($scope, $mdDialog, GadgetsService) {
  $scope.selected = [];
  $scope.query = {
    order: 'id',
    limit: 5,
    page: 1
  };

  $scope.addDialog = function(ev) {
    $mdDialog.show({
      controller: DialogController,
      templateUrl: 'public/Gadgets/_add_dialog.html',
      parent: angular.element(document.body),
      targetEvent: ev,
      clickOutsideToClose: true,
      fullscreen: true
    })
      .then(function(answer) {
        $scope.status = 'You said the information was "' + answer + '".';
      }, function() {
        $scope.status = 'You cancelled the dialog.';
      });
  };
  $scope.service = GadgetsService;
  $scope.service.init();
}
