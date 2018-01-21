dialog.factory('CompaniesDialogService', CompaniesDialogService);

function CompaniesDialogService($mdDialog, CompaniesService) {
  var service = {
    openAddCompanyDialog: openAddCompanyDialog,
    addCompany: addCompany,
    cancel: cancel,
    isCreate: false
  };


  return service;

  function cancel(){
    $mdDialog.cancel();
    service.editableDevice = {};
  }

  // Companies
  function openAddCompanyDialog(company, index){
    if (typeof company !== "undefined") {
      service.editedAt = index;
      service.isCreate = false;
    } else {
      service.isCreate = true;
    }

    $mdDialog.show({
      controller: CompaniesDialogController,
      templateUrl: 'public/Companies/_add_dialog.html',
      parent: angular.element(document.body),
      clickOutsideToClose: true,
      locals: {
        company: company
      },
      fullscreen: true
    });
  }

  function addCompany(company) {
    if (service.isCreate) {
      CompaniesService.addCompany(company);
    } else{
      CompaniesService.editCompany(company, service.editedAt);
    }
    cancel();
  }
}
