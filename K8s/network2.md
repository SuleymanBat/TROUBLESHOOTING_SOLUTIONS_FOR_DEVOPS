#### To create a bridge network on each node;

use following command;

>``ip link add v-net-0 type bridge``

Assign/Attach IP Address with following command;

>``ip link set dev v-net-0 up``

Set the IP address for the bridge interface like that;

>``ip addr add 10.244.1.1/24 dev v-net-0``

#### create veth pair

>``ip link add ...``

#### attach veth pair

>``ip link set ....``

#### Assign IP Address

>`` ip -n <namespace> addr add ....

>``ip -n <namespace> route add ....

#### Bring Up Interface

>``ip -n <namespace> link set ....


#### INSPECT THE KUBELET SERVICE AND IDENTIFY THE CONTAINER RUNTIME ENDPOINT VALUE IS SET FOR KUBERNETES

Run the command: 

>``ps -aux | grep kubelet | grep --color container-runtime-endpoint``

 and look at the configured --container-runtime-endpoint flag.

Use kubectl to fetch and show node information:

>``kubectl get nodes -o wide``

The output is similar to the following. The column CONTAINER-RUNTIME outputs the runtime and its version.

For Docker Engine, the output is similar to this:

NAME         STATUS   VERSION    CONTAINER-RUNTIME
node-1       Ready    v1.16.15   docker://19.3.1
node-2       Ready    v1.16.15   docker://19.3.1
node-3       Ready    v1.16.15   docker://19.3.1

You can check which socket you use by checking the kubelet configuration on your nodes.

Read the starting commands for the kubelet process:

>``tr \\0 ' ' < /proc/"$(pgrep kubelet)"/cmdline``

If you don't have tr or pgrep, check the command line for the kubelet process manually.

In the output, look for the --container-runtime flag and the --container-runtime-endpoint flag.

If the --container-runtime-endpoint flag is present, check the socket name to find out which runtime you use. For example, unix:///run/containerd/containerd.sock is the containerd endpoint.

ANOTHER WAY OF FINDING SOLUTION IS;

>``ps -aux | grep kubelet | grep network``

#### What is the path configured with all binaries of CNI supported plugins?

The CNI binaries are located under /opt/cni/bin by default.

#### Identify which of the below plugins is not available in the list of available CNI plugins on this host?
a)dhcp

b)vlan

c)cisco

d)bridge

Run the command: 

>``ls /opt/cni/bin``

 and identify the one not present at that directory.


 #### What is the CNI plugin configured to be used on this kubernetes cluster?

Run the command: 

>``ls /etc/cni/net.d/``

 and identify the name of the plugin.

 #### What binary executable file will be run by kubelet after a container and its associated namespace are created?

 Look at the type field in file /etc/cni/net.d/10-flannel.conflist.

 >``cat /etc/cni/net.d/10-flannel.conflist``

 #### Deploy weave-net networking solution to the cluster.

NOTE: - We already have provided a weave manifest file under the /root/weave directory.

Please check out the official weaveworks GitHub page for various weave releases, available at the top right panel.

Run the below command to deploy the weave on the cluster: -

>``kubectl apply -f /root/weave/weave-daemonset-k8s.yaml``

Now check if the weave pods are created and let's also check the status of our app pod now:

>``kubectl get pods -A | grep weave``
kube-system   weave-net-q7m6s                        2/2     Running   0          21s

>``kubectl get pods``
NAME   READY   STATUS    RESTARTS   AGE
app    1/1     Running   0          25m

#### What is the Networking Solution used by this cluster?

Check the config file located at /etc/cni/net.d/

>``ls /etc/cni/net.d/``

#### How many weave agents/peers are deployed in this cluster?

Run the command 

>``kubectl get pods -n kube-system``

 and count weave pods or

 >``k get pods -A | grep weave``

#### On which nodes are the weave peers present?

>``k get pods -A -o wide | grep weave``

#### Identify the name of the bridge network/interface created by weave on each node.

>``ssh node01 ifconfig | grep weave``

When you use Weave Net to create a virtual network for Docker containers or Kubernetes pods, Weave Net creates a virtual network interface on each node, and it uses the Linux bridge driver to manage traffic between containers on the same host and across hosts in the network.

By default, Weave Net names the bridge network/interface on each node "weave". However, you can change the name of the network interface by setting the "--name" flag when you start the Weave Net container. For example, if you start Weave Net with the command "sudo weave launch --name mynet", the bridge network/interface on each node will be named "mynet" instead of "weave".

Therefore, to identify the name of the bridge network/interface created by Weave on each node, you can run the command "ifconfig" or "ip link show" on each node, and look for the bridge interface with the name "weave" or the name that you specified with the "--name" flag.

#### What is the POD IP address range configured by weave?

Run the command 

>``ip addr show weave``

or try this;

>``ps -aux | grep weave``

or try this as an option;

>``k get pods -n kube-system``

later execute this command;

>``k logs -n kube-system weave-net-1232 <containername>``




#### What is the default gateway configured on the PODs scheduled on node01? Try scheduling a pod on node01 and check ip route output

SSH to the node01 by running the command: 

>``ssh node01``

 and then run the 
 
 >``ip route``
 
  command and look at the weave line.