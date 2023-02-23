## Identify the DNS solution implemented in this cluster.

Run the command: 

>``kubectl get pods -n kube-system``

 and look for the DNS pods. or alternatively;

 >``k get configmap -n kube-system ``

## How many pods of the DNS server are deployed?

Run the command: 

>``kubectl get deploy -n kube-system``

 and look for Desired count of coredns.

## What is the name of the service created for accessing CoreDNS?

Run the command: 

>``kubectl get service -n kube-system``

## What is the IP of the CoreDNS server that should be configured on PODs to resolve services?

Run the command: 

>``kubectl get service -n kube-system``

 and look for cluster IP value.


## Where is the configuration file located for configuring the CoreDNS service?

Inspect the Args field of the coredns deployment and check the file used.

Run the command: 

>``kubectl -n kube-system describe deployments.apps coredns | grep -A2 Args | grep Corefile``

## How is the Corefile passed into the CoreDNS POD?

Use the 

>``kubectl get configmap -n kube-system``

command for kube-system namespace and inspect the correct ConfigMap.
look at the coredns ConfigMap. It's passed through the ConfigMap volume in the deployment.

## What is the name of the ConfigMap object created for Corefile?

Run the command: 
>``kubectl get configmap -n kube-system ``

and identify the name.

## What is the root domain/zone configured for this kubernetes cluster?

Run the command: 

>``kubectl describe configmap coredns -n kube-system``

 and look for the entry after kubernetes.

## What name can be used to access the hr web server from the test Application? You can execute a curl command on the test pod to test. Alternatively, the test Application also has a UI. Access it using the tab at the top of your terminal named test-app. 

Use the command 

>``kubectl get svc``

 after viewing the available services, write the correct service name and port.

 ## We just deployed a web server - webapp - that accesses a database mysql - server. However the web server is failing to connect to the database server. Troubleshoot and fix the issue.They could be in different namespaces. First locate the applications. 

Run the command: 

>``kubectl edit deploy webapp``

 and correct the DB_Host value.

Set the DB_Host environment variable to use "mysql.payroll".

## From the hr pod nslookup the mysql service and redirect the output to a file /root/CKA/nslookup.out

Run the command: 

>``kubectl exec -it hr -- nslookup mysql.payroll > /root/CKA/nslookup.out``