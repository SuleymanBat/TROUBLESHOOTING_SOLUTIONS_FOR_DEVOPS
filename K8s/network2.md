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

#### What is the path configured with all binaries of CNI supported plugins?


