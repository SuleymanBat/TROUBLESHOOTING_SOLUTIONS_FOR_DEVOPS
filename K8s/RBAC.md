## WORKING WITH THE SCENARIOUS ABOUT RBAC(ROLE BASED ACCESS CONTROL) AUTHORIZATION

### WARMUP-1 

#### Inspect the environment and identify the authorization modes configured on the cluster.

Check the kube-apiserver settings.

Use the command;

´´´kubectl describe pod kube-apiserver-controlplane -n kube-system´´´

#### and look for --authorization-mode.
#### you can use grep also at the end of the code;

´´´kubectl describe pod kube-apiserver-controlplane -n kube-system | grep auth´´´

#### as the other option follow like that;
''' cat /etc/kubernetes/manifests/kube-apiserver.yaml '''

#### as the other option follow like that;
''' ps -aux | grep authorization '''

# WARMUP-2 

### How many roles exist in the default namespace?

Use the command to list the available roles in the default namespace.

´´´kubectl get roles´´´


### How many roles exist in all namespaces together?

´´´ kubectl get roles --all-namespaces ´´´
´´´ kubectl get roles -A ´´´

### Also you can add at the end of the code for counting the number of lines like that;

''' kubectl get roles --all-namespaces --no-headers | wc -l '''

# WARMUP-3

### What are the resources the kube-proxy role in the kube-system namespace is given access to?

## INFO:
The kube-proxy role in the kube-system namespace is given access to the following Kubernetes resources:

> endpoints

> nodes

> pods

> services

It also has the ability to perform the following actions:

> watch

> list

> update

> create

> delete

These permissions allow the kube-proxy to watch for changes to the Kubernetes network and update the network routing rules accordingly.

Please execute the command below to see which resources kube-proxy role perform on;

'''kubectl describe role kube-proxy -n kube-system'''

# WARMUP-4

#### WHAT ACTIONS CAN THE KUBE-PROXY ROLE PERFORM ON CONFIGMAPS?

if we execute and see the output of the below command, we can reach the necessary info easily.

'''kubectl describe role kube-proxy -n kube-system'''

# WARMUP-5

#### WHICH ACCOUNT KUBE-PROXY ROLE ASSIGNED TO IT?

For that we need to look at "role binding" as below command;
''' kubectl get rolebindings -n kube-system '''

''' kubectl describe rolebindings kube-proxy -n kube-system '''

# WARMUP-6

###### A user "dev-user" is created. User's details have been added  to the "kubeconfig" file. Inspect the permissions granted to the users. Check if the user can list pods in the "default" namespace. Use the "--as dev-user" option with "kubectl" to run commands as the "dev-user".

First let's look at the config file with the command below;

'''kubectl config view'''

'''kubectl get pods --as dev-user'''

# WARMUP-7

###### Create the necessary roles and rolebindings required for the "dev-user" to create, list and delete pods in the "default" namespace. Use the given spec:

> Role:developer

> Role Resources: pods

> Role Actions: list

> Role Actions: create

> Role Actions: delete

> RoleBindings: dev-user-binding

> RoleBindings: Bound to dev-user

###### First we have to create role and rolebindings  for the dev-user

> ''' kubectl create role --help '''
Here we can research the examples of usages. It gives idea.

> ''' kubectl create role developer --verb=list,create,delete --resource=pods'''

> ''' kubectl describe role developer'''

This time we will do the same for "rolebinding" as below;
> '''kubectl create rolebinding --help'''
Here we can research the examples of usages. It gives idea how to we approach.

> '''kubectl create rolebinding dev-user-binding --role=developer --user=dev-user'''

> ''' kubectl describe rolebinding dev-user-binding'''

# WARMUP-8

#### The "dev-user" is trying to get details about the "dark-blue-app" pod in the "blue" namespace. Investigate and fix the issue. We have created the required roles and rolebindings but something seems to be wrong.

As a dev-user I will going to get details about the app as below;
> ''' kubectl --as dev-user get pod dark-blue-app -n blue '''

Let's take a look at the roles in the blue namespace as below;
> ''' kubectl get roles -n blue '''

> ''' kubectl get rolebindings -n blue '''

> ''' kubectl describe role developer -n blue '''

When we look at the resource name We saw the name written wrongly. For the aim of correct we will edit  like that;
> kubectl edit role developer -n blue

Now We can change the resource name as "dark-blue-app" from VIM editör.

If we apply code as below for the aim of control again;
>''' kubectl --as dev-user get pod dark-blue-app -n blue'''

We can see it is running.

# WARMUP-9

##### GRANT THE "DEV-USER" PERMISSIONS TO CREATE DEPLOYMENTS IN THE "BLUE" NAMESPACE. REMEMBER TO ADD FOR API GROUP "APPS".

As the "dev-user" I want to create "deployment" like below;
> '''kubectl --as dev-user create deployment nginx --image=nginx -n blue'''

When we try to do that, it says the user "dev-user" can not create resource deployments in API group "apps" in the "blue" namespace.
What we have to do is;
> '''kubectl edit role developer -n blue '''

When the VIM editör opens, we will copy and paste "the block of apiGroups" for "apps"

Let's verify that;
> '''kubectl role developer -n blue'''

>'''kubectl --as dev-user create deployment nginx --image=nginx -n blue'''
