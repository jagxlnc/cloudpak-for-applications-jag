print "Updating application CustomerOrderServicesApp..."

parms = "-operation update"
parms += " -contents /work/config/CustomerOrderServicesApp.ear"
parms += " -usedefaultbindings"
parms += " -nodeployejb"
app = AdminApp.update("CustomerOrderServicesApp", "app", [parms])

AdminConfig.save()
