companies.factory('CompaniesService', CompaniesService);

function CompaniesService($q, $filter, Ajax) {

  var companiesEndpoint = 'api/companies/';

  var service = {
    init: init,
    addCompany: addCompany,
    removeCompany: removeCompany
  };

  return service;

  function init() {
    var defer = $q.defer();
    service.companies = [];
    var promisses = {};
    promisses.companies = Ajax.get(companiesEndpoint);
    $q.all(promisses).then(function(result) {
      console.log(result);
      service.companies = result.companies.data;
    }, function(error){
      defer.reject(error);
    });
    return defer.promise;
  }


  function addCompany(company) {
    var promisse;
    promisse = Ajax.post(companiesEndpoint, company);
    promisse.then(success, error);
    return promisse;

    function success(result) {
      service.companies.push(result.data);
    }

    function error(result) {
      console.log(result);
    }
  }

  function editCompany(company, index) {
    var promisse;
    promisse = Ajax.put(companiesEndpoint, company);
    promisse.then(success, error);
    return promisse;

    function success(result) {
      var updatedCompany = result.data;
      service.companies[index] = updatedCompany;
    }

    function error(result) {
      console.log(result);
    }
  }

  function removeCompany(company, index) {
    var promisse;
    promisse = Ajax.delete(companiesEndpoint, company.id);
    promisse.then(success, error);
    return promisse;

    function success(result) {
      service.companies.splice(index,1)
    }

    function error(result) {
      console.log(result);
    }
  }
};
