Let's start with a host with Docker installed on it. This host has a set of its own processes running, such as a number of operating system processes, Docker daemon itself, the SSH server etc. We will run an Ubuntu Docker container with this command;

> `` docker run ubuntu sleep 3600 ``

that runs a process that sleeps for an hour.

We know that unlike virtual machines, containers are not completely isolated from their host. Containers and the host share the same kernel.Containers are isolated using namespaces in Linux. The host has a namespace and the containers have their own namespace. All the processes run by the containers are in fact run on the host itself but in their own namespace. As far as the Docker container is concerned, it is in its own namespace and it can see its own processes only.It can not see anything outside of it or in any other namespace.So  when you list the processes from within the Docker container, you see the sleep process with a process ID of one.As below;

> `` ps aux ``

For the Docker host, all processes of its own, as well as those in the child namespaces are visible as just another process in the system.So when you list the processes on the host, you see a list of processes, including the sleep command but with a different process ID.This is because the processes can have different process IDs in different namespaces and that's how Docker isolates containers within a system. So that's process isolation. The Docker host has a set of users, a root user as well as a number of non-root users.By default Docker run processes within containers as the root user. Both within the container and outside the container on the host, the process is run as the root user. If you do not run the process within the container to run as the root user you may set the user using the user option within the Docker run command and specify the new user ID. As below;

> ``docker run --user=6666 ubuntu sleep 2400``

You will see that the process now runs with the new user ID. If you check the command below like that;

> ``ps aux``

Another way to enforce user security is to have this defined in the Docker image itself at the time of creation.For example we will use the default Ubuntu image and set the user ID to 5000 using the user instruction.

###### Dockerfile

> ``FROM ubuntu``

> ``USER 5000``

Then build the custom image like that;

> ´´docker build -t sample-ubuntu-image .``

We can now run this image without specifying the user ID ;

>> ``docker run sample-ubuntu-image sleep 2400``

and the process will be run with the user ID 5000. Check this as below;

>> ``ps aux``

What happens when you run containers as the root user? Is the root user within the container the same as the root user on the host? Can the process inside the container do anything that the root user can do on the system?If so, is not that dangerous? Docker implements a set of security features that limits the abilties of the root user within the container. So the root user within the container is not really like the root user on the host. Docker uses Linux capabilities to implement this. You can see a full list of capabilities of root user at this location;

> ``/usr/include/linux/capability.h``

You can now control and limit what capabilities are made available to a user. By default Docker run a container with a limited set of capabilities. If you want to add some priviledges you can execute below command;

> ``docker run --cap-add MAC_ADMIN ubuntu``

Similarly you can drop privileges as well using;

> ``docker run --cap-drop KILL ubuntu``

Incase you wish to run container with all privileges enabled;

> ``docker run --privileged ubuntu``

In Kubernetes containers are encapsulated in PODs.You may choose to configure the security settings at a container level or ata  POD level. If you configure it at a POD level the settings will carry over to all the containers within the pod. If you configure it at both the POD and the container, the settings on the container will override the settings on the POD. In the Pod Definition file; To configure security context on the container, add a field called "security context" under the "spec" section of the POD. Use the "runAsuser" option to set the user ID for the POD.

To set the same configuration on the container level move the whole section under the container specification and put right below "spec".

Capabilities are only supported at the container level and not at the POD level.