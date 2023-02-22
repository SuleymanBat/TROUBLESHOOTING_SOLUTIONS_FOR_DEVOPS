#### What network range are the nodes in the cluster part of?





#### How many Nodes are part of this cluster? Including master and worker nodes

Run the command 

>``kubectl get nodes``

#### What is the Networking Solution used by this cluster?

Check the config file located at /etc/cni/net.d/

>``ls /etc/cni/net.d/``

#### How many weave agents/peers are deployed in this cluster?

>``k get pods -A -o wide | grep weave``

#### Identify the name of the bridge network/interface created by weave on each node.

>``ssh node01 ifconfig | grep weave``

When you use Weave Net to create a virtual network for Docker containers or Kubernetes pods, Weave Net creates a virtual network interface on each node, and it uses the Linux bridge driver to manage traffic between containers on the same host and across hosts in the network.

By default, Weave Net names the bridge network/interface on each node "weave". However, you can change the name of the network interface by setting the "--name" flag when you start the Weave Net container. For example, if you start Weave Net with the command "sudo weave launch --name mynet", the bridge network/interface on each node will be named "mynet" instead of "weave".

Therefore, to identify the name of the bridge network/interface created by Weave on each node, you can run the command "ifconfig" or "ip link show" on each node, and look for the bridge interface with the name "weave" or the name that you specified with the "--name" flag.