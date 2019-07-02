# Deployment yaml for OpenShift

## Cluster config
Create a new SCC using `ssc.yaml`

```
oc apply -f ssc.yaml
```

## Namespace config
Create a new service account and bind to the SCC. It is assumed the namespace is `appmod-twas`

```
oc create serviceaccount websphere -n appmod-twas

oc adm policy add-scc-to-user ibm-websphere-scc -z websphere -n appmod-twas
```

## Deploy
Namespace `appmod-twas`, name `cos-twas` and the image are hardcoded in these yaml files. Update them as necessary

```
oc apply -f dc.yaml -n appmod-twas
oc apply -f service.yaml -n appmod-twas
oc apply -f route.yaml -n appmod-twas
```

The result is:
-  a Deployment Config for the application with `liveness` and `readiness` probes, a `serviceaccount` set to `websphere` and a `securityContext` set as required
- a service for ports `9080` and `9443`
- a route 
