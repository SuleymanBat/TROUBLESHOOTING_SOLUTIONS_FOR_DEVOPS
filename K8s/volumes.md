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


### WARMUP 5: