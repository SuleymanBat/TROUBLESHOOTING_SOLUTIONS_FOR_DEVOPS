#### What is the network interface configured for cluster connectivity on the controlplane node?node-to-node communication

>``ip a``

>``ip link``





#### What is the MAC address of the interface on the controlplane node?

> ``ip link show eth0``

#### What is the IP address assigned to node01?

Run the command: 

>``kubectl get nodes -o wide``

 and look for IP assigned to node01 node.

#### What is the MAC address assigned to node01?

SSH to the node01 node and run the command: 

>``ssh node01 ip link show eth0``

#### Let's say We use Docker as our container runtime. What is the interface/bridge created by Docker on this host?

Docker creates a bridge network by default when it is installed on a host. The name of this bridge network is typically "docker0".

You can confirm the existence of the Docker bridge network on your host by running the following command:

> ``docker network ls``

This will list all the networks created by Docker, including the default bridge network. If you want to view detailed information about the docker0 network, you can use the docker network inspect command:

>``docker network inspect bridge``

This command will output a JSON-formatted description of the bridge network, which includes information about its configuration, such as the subnet range and gateway address.

>``ssh node01 ifconfig -a``

Here are some examples of commands you can use to get network interface information:

>``ip addr show``

 - This command displays information about all network interfaces on the system, including their IP addresses, netmasks, and MAC addresses.

``ip link show``

 - This command displays a list of all network interfaces on the system, including their names and states.

``netstat -i``

 - This command displays a list of all network interfaces on the system, including statistics such as packets in/out and errors.

``ethtool eth0``

 - This command displays information about a specific network interface, such as its speed and duplex settings.

``cat /proc/net/dev``

 - This command displays statistics for all network interfaces on the system, including bytes in/out, packets in/out, and errors.

#### If you were to ping google from the master node, which route does it take? What is the IP address of the Default Gateway?

in general, the IP address of the default gateway can be found by running the command "ipconfig" on Windows or "ifconfig" on Linux or macOS from the command line. The output of these commands will show the IP address of the default gateway, along with other network information such as the IP address of the device itself and the subnet mask.

>``ip r``

#### What is the port the kube-scheduler is listening on in the master node?

By default, kube-scheduler in a Kubernetes cluster listens on port 10251 for secure communication and port 10259 for insecure communication on the master node.

Specifically, the secure port (10251) is used for communication between the kube-scheduler and the Kubernetes API server, which is responsible for managing the state of the Kubernetes cluster. The insecure port (10259) is used for read-only access to the scheduling state of the kube-scheduler, and can be used for debugging and monitoring purposes.

>``netstat -natulp | grep kube-scheduler``

#### Notice that ETCD is listening on two ports. Which of these have more client connections established?

By default, the ETCD server listens on port 2379 for client communication and port 2380 for server-to-server communication. The vast majority of client requests to ETCD are expected to go to port 2379, including reads, writes, and watch operations. In most cases, port 2380 is only used for server-to-server communication, such as when ETCD nodes need to communicate with each other to maintain cluster consistency.

>``netstat -natulp | grep etcd | grep LISTEN``

or

>`` netstat -anp | grep etcd | grep 2380 | wc -l ``

>``netstat -anp | grep etcd | grep 2379 | wc -l ``




