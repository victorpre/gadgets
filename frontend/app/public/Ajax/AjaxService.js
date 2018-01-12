angular.module('ajax').factory('Ajax', Ajax);
function Ajax($http){

  var baseUrl = "http://localhost:8000/"
  var model = {
    get: get,
    post: post,
    delete: del,
  };

  return model;

  function get(url, params){
    if(!params){
      params = {};
    }
    return $http({
      method: 'GET',
      url: baseUrl+url,
      params: params
    });
  }

  function post(url, params){
    if(!params){
      params = {};
    }
    return $http({
      method: 'POST',
      url: url,
      data: params
    });
  }

  function del(url, params){
    if(!params){
      params = {};
    }
    return $http({
      method: 'DELETE',
      url: url,
    });
  }
}