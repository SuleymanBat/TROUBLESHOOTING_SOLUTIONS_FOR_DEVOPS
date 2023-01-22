# SERVICE ACCOUNTS

Service Accounts in K8s is limked to other security related concepts in K8s such as authentication, authorization, role-based access controls, etc.
There are two types of accounts in K8s(user account and service account). User account used by humans and service account used by machines. A User Account could be an administrator accessing the cluster to perform administrative tasks or a developer accessing the cluster to deploy applications. A service could be an application to interact with a K8s cluster. For example, a monitoring application like Prometheus uses a service account to pull the K8s API for performance metrics. An automated build tool like Jenkins uses service accounts to deploy apps on the K8s cluster.  

Let's take an example;
I've built a simple Kubernetes dashboard app named "My Kubernetes Dashboard". It is a simple application built in Python. All that it does when deployed is retrieve the list of pods on K8s cluster by sending a request to the K8s API, and displayed on a webpage. In order to query my app the Kubernetes API, it has to be authenticated. For that we use a service account. To create a service account, run the command as below;

> `` kubectl create serviceaccount dashboard-sa ``

To view the service accounts from the kubectl, run the command below;

> `` kubectl get serviceaccount``

When the service account is created it also creates a token automatically. Service Account token must be used by the extrernal application while authenticating to the Kubernetes API. The Token is stored as a "secret object". If you run below command you can see the Token details like that;

> `` kubectl describe serviceaccount dashboard-sa``

When a service account is created, it first creates the "service account object" and then generates a "token" for the service account. It then creates a "secret object" and stores that token inside the secret object. The secret object is then linked to the service account. To view the token, view the secret object by running the command;

> `` kubectl describe secret dashboard-sa-token-kbbdm ``

This token can then be used as an authentication bearer token, while making a risk call to the Kubernetes API. For example, in this simple example using curl;

> `` curl https://172.168.31.23:6443/api``

For example, in this simple example using curl you could provide the bearer token as an authorization header while making a risk call to the Kubernetes API. 

> `` curl https://172.168.31.23:6443/api -insecure --header "Authorization: Bearer klerJyvWPaacåwÖÄäas...."

In case of my custom dashboard application, copy and paste the token into the tokens field   to authenticate the dashboard application.

You can create a Service Account, assign the right permissions using role-based access control mechanism, and export your service account tokens and use it to configure your third party application to athenticate to the Kubernetes API. But what if your third party app is hosted on the K8s cluster itself? For example, we can have our custom K8s dashboard app or the Prometheus app, deployed on the K8s cluster itself. In that case this whole process of exporting the service account token and configuring the third party app to use it, can be made simple by automatically mounting the service token secret as a volume inside the pod hosting the third party app. That way the token to access the K8s API is already placed inside the pod and can be easily read by the app. If you look at the list of service accounts by running command below;

> `` kubectl get serviceaccount``

you can see that there is a default service account that exists already. For every namespace in K8s, a service account named default is automatically created. Each namespace has its own default service account. Whenever a pod is created, the default service account and its token are automatically mounted to that pod as a volume mount. 

From inside the pod if you run the "ls" command to list the contents of the directory as below;

> ``kubectl exec -it my-kubernetes-dashbord ls /var/run/secrets/kubernetes.io/serviceaccount``

you will see the secret mounted as three seperate files.like that;

> ´´ ca.crt namespace token ´´

If you see the content of "token" like that;

> ``` kubectl exec -it my-kubernetes-dashbord cat /var/run/secrets/kubernetes.io/serviceaccount/token ```

you will see the token to be used for accessing the K8s API.

If you would like to use a different service account, modify the pod definition file(pod-definition.yml) to include a service account field  and specify the name of the new service account. Remember you can not edit the existing service account. You must delete and recreate the pod. However, in case od a deploymnent, you will be able to the service account as any changes to the pod definition file automatically trigger a new rollout for the deployment.So the deployment will take care of deleting and recreating new pods with the right service account.

IMPORTANT: 
Version 1.22 contributed some changes in this process. The authomatic mounting of the secret object to the pod was changed and instead it then moved to the "token request API".
With Version 1.24, a change was made where when you create a service account, it  no longer authomatically creates a secret or a token as a secret. So you must run the command;

> ```` kubectl create token dashboard-sa ````

If you tahe this token and decode, this time you will see that it has an expiry date defined.

# WARMUP-1.

###### How many Service Accounts exist in the default namespace?

> ```` k get serviceaccount ````

# WARMUP-2:

###### What is the secret token used by the default service account?####### CLUE:Run the command kubectl describe serviceaccount default and look at the Tokens field.

> ````k describe serviceaccount default````

# WARMUP-3:
###### We just deployed the Dashboard application. Inspect the deployment. What is the image used by the deployment?

> ````k describe deployment````

# WARMUP-4:
###### Identify the serviceaccount name mounted on Web-dashboard application?

> ````kubectl get po -o yaml | grep service````

# WARMUP-5:
###### At what location is the ServiceAccount credentials available within the pod?

> First Approach: ```` k describe pod ````

> Second Approach: ```` kubectl get po -o yaml | grep mount ````

# WARMUP-6:
##### The application needs a ServiceAccount with the Right permissions to be created to authenticate to Kubernetes. The default ServiceAccount has limited access. Create a new ServiceAccount named dashboard-sa.

> ````k create serviceaccount dashboard-sa````

# WARMUP-7:
###### Create an authorization token for the newly created service account, copy the generated token and paste it into the token field of the UI.

###### To do this, run kubectl create token dashboard-sa for the dashboard-sa service account, copy the token and paste it in the UI.

> ```` k create token dashboard-sa  ````

# WARMUP-8:
##### You shouldn't have to copy and paste the token each time. The Dashboard application is programmed to read token from the secret mount location. However currently, the default service account is mounted. Update the deployment to use the newly created ServiceAccount

Edit the deployment to change ServiceAccount from default to dashboard-sa.

> ````kubectl set serviceaccount deploy/web-dashboard dashboard-sa````

> Second alternative method: ````k edit deployment web-dashboard````
