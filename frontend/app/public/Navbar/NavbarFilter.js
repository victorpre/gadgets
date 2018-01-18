navbar.filter('validPath', NavbarFilter);

function NavbarFilter() {
  return function(data) {
    var list = [];
    angular.forEach(data, function(v){

      if((angular.isUndefined(v.abstract) && v.name)) {
        list.push(v);
      }
    });
    return list;
  }
}
