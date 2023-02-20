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

