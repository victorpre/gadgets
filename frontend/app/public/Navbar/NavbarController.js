navbar.controller('NavbarController', NavbarController );

function NavbarController($scope, $mdSidenav) {

  $scope.openLeftMenu = function() {
    $mdSidenav('left-menu').toggle();
  }
}
