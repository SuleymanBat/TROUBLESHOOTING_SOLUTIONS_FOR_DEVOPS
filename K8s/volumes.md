### WARMUP 1:
##### The application stores logs at location /log/app.log. View the logs.

You can exec in to the container and open the file:

> ``kubectl exec webapp -- cat /log/app.log``

### WARMUP 2:
##### Configure a volume to store these logs at /var/log/webapp on the host.

Use the spec provided below.

- Name: webapp

* Image Name: kodekloud/event-simulator

* Volume HostPath: /var/log/webapp

* Volume Mount: /log

We are going to edit the pod. 

> ``k edit pod webapp``

In the upcoming page we should put the necessary volume info under the "volume" ;

> ``  - name: log-volume``

    hostPath:
      # directory location on host
      path: /var/log/webapp``

At the same time we should add "mountPath" under the "volumeMounts" as below;

>``volumeMounts: ``

    - mountPath: /log
      name: log-volume


> ``k replace --force -f /tmp/kubectl-edit-24578.yaml``

Let's check the pod;

>`` cd /var/log/webapp``

>``ls``

### WARMUP 3:Create a Persistent Volume with the given specification.


Volume Name: pv-log

Storage: 100Mi

Access Modes: ReadWriteMany

Host Path: /pv/log

Reclaim Policy: Retain



### WARMUP 4: Let us claim some of that storage for our application. Create a Persistent Volume Claim with the given specification.


Volume Name: claim-log-1

Storage Request: 50Mi

Access Modes: ReadWriteOnce


# TASK: Your team has deployed on Kubernetes a simple app which generates a static page with resources and writes it to a mounted volume.The app generates the following files and directories on the mounted drive:
- index.html - the specifying the static page
- css/ - directory containing stylesheet assets 
- img/ - directory containing images served on the page

The app runs on K8s as a Pod and mounts a persistent volume named "webpage".
The team has asked you to deploy the Pod, which will mount the persistent volume and will serve the page.
Write a Kubernetes Pod Definition according to the expectations listed below:
-The Pod has the name "webpage-server"
-The Pod runs a single container called "nginx" which uses the image "nginx:1.15;
-The container exposes port 80;
-The container mounts the "webpage" persistent volume on the path "/var/www/html;
-The volume is mounted in "read-only" mode

For this test assume that:
-The Pod will be created in the "default" namespace(it is not expected to define a namespace)
-Your solution will be applied using kubectl apply -n default -f solution.yaml

this task's solution is in the "volume-solution.yaml" Please find that in the same directory.

