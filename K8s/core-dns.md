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


