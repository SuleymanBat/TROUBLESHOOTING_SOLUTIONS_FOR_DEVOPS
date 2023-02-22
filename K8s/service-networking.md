### What network range are the nodes in the cluster part of?

Run the command: 

>``ip addr``

 and look at the IP address assigned to the eth0 interfaces. Derive network range from that.

 AS A SECOND Solution you can;
 make use of the ipcalc utility. If it is not installed, you can install it by running: 
 
 >``apt update``
 
  and the 
  
>``apt install ipcalc``

Then use it to determine the network range as shown below:

>``ip a | grep eth0``

### What is the range of IP addresses configured for PODs on this cluster? First, find the Internal IP of the nodes.

The network is configured with weave. Check the weave pods logs using the command 

>``kubectl logs <weave-pod-name> weave -n kube-system``

 and look for "ipalloc-range".

### What is the IP Range configured for the services within the cluster?

##### Solution1;
Inspect the setting on kube-api server by running on command 

>``cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep cluster-ip-range``

##### Solution2;

>``k cluster-info dump | grep cluster-ip-range``

### How many kube-proxy pods are deployed in this cluster?

###### Solution1;

>``k get pods -A``

###### Solution2;
Run the command: 

>``kubectl get pods -n kube-system``

 and look for kube-proxy pods.


 ### What type of proxy is the kube-proxy configured to use?

 Check the logs of the kube-proxy pods. Run the command: 
 
 >``kubectl logs <kube-proxy-pod-name> -n kube-system``

### How does this Kubernetes cluster ensure that a kube-proxy pod runs on all nodes in the cluster? Inspect the kube-proxy pods and try to identify how they are deployed.

To ensure that a kube-proxy pod runs on all nodes in a Kubernetes cluster, a DaemonSet is typically used. A DaemonSet is a Kubernetes object that ensures that a copy of a specified pod is running on every node in a cluster.

To inspect the kube-proxy pods and identify how they are deployed, you can use the following command:

>``kubectl get daemonset kube-proxy -n kube-system -o yaml``

This command will display the kube-proxy DaemonSet configuration in YAML format, including the pod template that specifies how the kube-proxy pods are deployed.

The DaemonSet ensures that one kube-proxy pod is running on each node in the cluster. If a new node is added to the cluster, the DaemonSet automatically creates a new kube-proxy pod on that node. If a node is removed from the cluster, the DaemonSet ensures that the corresponding kube-proxy pod is also removed.