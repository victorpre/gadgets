navbar.controller('NavbarController', NavbarController );

function NavbarController($scope, $state, validPathFilter, $mdSidenav) {

  $scope.links = validPathFilter($state.get());
  $scope.toggleLeftMenu = function() {
    $mdSidenav('left-menu').toggle();
  }
}
