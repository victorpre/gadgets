angular.module('ajax').config(config);

function config($httpProvider){
  $httpProvider.defaults.headers.common['X-CSRFToken'] = 'csrftoken'; // alguem precisa ter setado isso aqui!
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/json';
}
