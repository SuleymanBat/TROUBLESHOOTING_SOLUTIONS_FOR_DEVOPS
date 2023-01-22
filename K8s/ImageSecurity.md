## WARMUP 1:
##### WHAT SECRET TYPE MUST WE CHOOSE FOR "docker registry"?

If you look at the different types of secrets by executing command like that;

> ````k create secret````

## WARMUP 2:
### WE HAVE AN APPLICATION RUNNING ON OUR CLUSTER. LET US EXPLORE IT FIRST. WHAT IMAGE IS THE APPLICATION USING?

> ````k get deploy````

> ````k describe deploy web````


## WARMUP 3:
#### We decided to use a modified version of the application from an internal private registry. Update the image of the deployment to use a new image from "myprivateregistry.com:5000" 

We know that if you do not specify a registry before the image name it is going to default it is going to pull from the default location on Docker Hub. So what we want to do is we want to edit the deployment as below command;

> ````k edit deployment````

When Vim editör of deployment file open we must add "myprivateregistry.com:5000" to the "image row" under spec and then later under containers right before nginx:alpine. Like that;

> ````- image: myprivateregistry.com:5000/nginx:alpine````

And then we can check it out as below;

> ````k describe deploy web````

## WARMUP 4:
#### Are the new PODs created with the new images successfully running?

> ````k get pods````

> ````k describe pod web````

If we look at the "events" section, it says "fail to pull image", "malformed response", that is basically because it does not have the permissions to pull image from that repository. 

## WARMUP 5:
##### Create a secret object with the credentials required to access the registry.

Name: private-reg-cred

Username: dock_user

Password: dock_password

Server: myprivateregistry.com:5000

Email: dock_user@myprivateregistry.com

Secret: private-reg-cred
Secret Type: docker_registry
Secret Data

> ````k create secret docker-registry -h````

> ````kubectl create secret docker-registry private-reg-cred --docker-server=myprivateregistry.com:5000 --docker-username=dock_user --docker-password=dock_password --docker-email=dock_user@myprivateregistry.com````

## WARMUP 6:
#### Configure the deployment to use credentials from the new secret to pull images from the private registry

> ``k edit deployment web``

in the VIM editör we must add a block under the spec  like that;

> ``imagePullSecrets:`` 
> ``- name: private-reg-cred``

check with this command;
> ``k describe deployment web`` 


