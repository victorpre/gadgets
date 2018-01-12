gadgets.controller('GadgetsController', GadgetsController );

function GadgetsController(GadgetsService) {
  var ctrl = this;
  ctrl.service = GadgetsService;
  ctrl.service.init();
}
