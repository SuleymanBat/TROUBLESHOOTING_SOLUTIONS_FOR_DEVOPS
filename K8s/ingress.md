You build the application into a Docker image and deploy it on the Kubernetes Cluster as a pod in the Deployment. Your application needs a Database so you deploy a MySQL database as a pod and creeate a service  of type cluster IP called mySQL Service to make it accessible to our application. Your application is now working. To make the application accessible to the outside world you crate another service, this time of type NodePort and make your application available on a high port on the nodes in the cluster. 

Whenever the traffic increases we increase the number of replicas of the pod to handle the additional traffic, and the service takes care of splitting traffic between the pods. However if you have deployed a production-grade app before, you know that there are many more things involved in addition to simply splitting the traffic between the pods. 

For example, we do not want the users to have to type in the IP address every time. So you configure your DNS Server to point to the IP of the nodes. Your users can now access your application using the URL and port. You do not want users used to have to remember port number either. However, service node ports can only allocate high numbered ports which are greater than 30000. So you then bring in an additional layer of between tghe DNS server and your cluster like a proxy server that proxies request on port 80 to port 38080 on your nodes. You then you point DNS to this server and users can now access your application by simply visiting just URL( like mydevopsjourney.com). Now this is if your application is hosted on-prem in your data center. 

Let's see what you could do if you were on "public cloud environment" like "Google Cloud platform".
In that case, instead of creating a service of type nodePort for your application, you could set it type "Load balancer".When you do that, kubernetes would still do everything that it has to do for a nodePort which is to provision a high port for the service. But in addition to that, kubernetes also sends a request to "Google Cloud platform" to provision a network load balancer for the service. On receving the request, GCP will then automatically deploy a "Load Balancer" configured to route traffic to the service ports on all nodes and return its information to Kubernetes. The Load Balancer has an external IP that can be provided to users to access the application.In this case, we set the DNS to point to this IP and users access the application using the URL, mydevopsjourney.com.

Your company's business grows and you now have new services for your customers. For example, a video streaming service. Now you want your users to be able to access your new video streaming service by going to mydevopsjourney.com/watch. You would like to make your old app accessible at mydevopsjourney.com/history. Your developers developed the new video streaming app as a completely different app as it has nothing to do with the existing one. However, to share the cluster's resources, you deploy the new app as a seperate deployment within the same cluster. You create a service called "video service" of type "Load Balancer". Kubernetes provision support 38282 for this service and also provisions a network load balancer on the cloud. The new load balancer has a new IP. Remember, you must pay for each of these load balancers and having many such load balancerscan inversely affect your cloud bill. So how do you direct traffic between each of these load balancers based on the URL that the user types in? You need yet another proxy or load balancer that can redirect traffic based on URLs to the different services. Every time you introduced a new service, you have to reconfigure the load balancer. 

And finally, you also need to enable SSL for your applications. SSL stands for Secure Sockets Layer, which is a protocol used to establish a secure and encrypted communication channel between a web server and a web browser. It has been succeeded by Transport Layer Security (TLS) which is the current protocol used for securing communication over the internet.

The SSL/TLS protocol is used to encrypt data during transmission to prevent unauthorized access, interception or tampering. When you access a website using HTTPS (Hypertext Transfer Protocol Secure), the SSL/TLS protocol is used to encrypt the data exchanged between your browser and the web server. This ensures that any sensitive information such as login credentials, credit card numbers or other personal information is transmitted securely and cannot be intercepted by attackers.

So your users can access your app using https. Where do you configure that? It can be done at different levels, either at the application level itself, or at the load balancer level, or at the proxy server level, but which one? Now you do not want your developers to implement it in their apps as they would do it in different ways, and it is an additional burden for them to develop additional code to handle that. You want it to be configured in one place with minimal mainteanance. Now, that's a lot of different configuration and all of these becomes difficult  to manage when your app scales. It requires involving different individuals and different teams. You need to configure your firewall rulesfor each new service, and it's expensive as well as for each service, a new cloud-native load balancer needs to be provisioned. Wouldn't it be nice if you could manage all of that within the Kubernetes cluster  and have all that configuration  as just another Kubernetes definition file that lives along with the restof your app deployment files?That's where ingress comes in.

Ingress helps your users access your application using a single externally accessible URL that you can configure to route traffic to different services within your cluster based on the URL path. At the same time implement SSL security as well. Think of Ingress as a Layer 7 load balancer built into the Kubernetes cluster that can be configured using native Kubernetes primitives just like any other object that we have been working with  in K8s. Even with Ingress you still need to expose it to make it accessible outside the cluster, so you still have to either publish it  as a "nodePort" or with a cloud native "LoadBalancer" but that is just a one-time configuration. You are going to perform all your load balancing  of SSL and URLbased routing configurations on the Ingress controller. 

Without Ingress How would you do all of this?
Ingress is a specific software application developed by Google for managing access to resources in a network. Its primary function is to control and secure access to network resources by enforcing authentication, authorization, and accounting policies.

If you wanted to perform the same functions as Ingress without using that specific software application, you would need to identify alternative solutions that could fulfill the same requirements. 

Use a different access control solution: There are many other software applications and tools available that can be used to control access to network resources, such as firewalls, proxy servers, and virtual private networks (VPNs). Each of these solutions has its own set of strengths and weaknesses, and the best choice will depend on your specific use case and requirements.Some potential options might include: NGINX or HAproxy or Traefik. 

I would deploy them on my K8s cluster  and configure them to route traffic to other services. The configuration involves defining URL routes, configuring SSL certificates etc. Ingress is implemented by K8s in kind of the same way. You first deploy a supported solution which happens to be any of these listed here, and then specify a set of rules to configure Ingress. The solution you deployed is called an "Ingress controller" and set of rules you configure  are called as "Ingress resources". Ingress resources are created using definition files like the ones we have been using to create pods, deployments and services earlier.

A K8s cluster does mot come with an Ingress controller by default. So you must deploy one "Ingress controller". What do you deploy? There are many options.(GCP HTTP(S) Load Balancer(GCE), NGINX, Contour, HAPROXY, traefik,Istio) Let's say we preffered NGINX and now we should configure deployment definition file named NGINX ingress controller.

"""
apiVersion: apps/v1

kind: Deployment

metadata:

  name: nginx-ingress-controller

spec:

  replicas: 1

  selector:

    matchLabels:

      app: nginx-ingress

  template:

    metadata:

      labels:

        name: nginx-ingress

    spec:

      containers:

      - name: nginx-ingress-controller

        image: nginx:1.14.2

      args:
        - /nginx-ingress-controller
        - --configmap=$(POD_NAMESPACE) / nginx-configuration

      env:
        - name: POD_NAME
          valueFrom:
          fieldRef:
            fieldPath: metadata.name
        - name: POD_NAME
          valueFrom:
          fieldRef:
            fieldPath: metadata.name
      ports:
        - name: http
          containerPort: 80
        - name: https
          containerPort: 443
"""
 
 Inorder to decouple configuration data from the NGINX controlller image, you must create a "ConfigMap" object and pass that in. 
'''
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-configuration
'''

We then need a "service" to expose the Ingress controller to the external world so we create a service of type nodePort with the NGINX Ingress label selector as below;

'''
apiVersion: v1
kind: Service
metadata:
  name: nginx-ingress
spec:
  type: NodePort
  selector:
    name: nginx-ingress
  ports:
      # By default and for convenience, the `targetPort` is set to the same value as the `port` field.
    - port: 80
      targetPort: 80
      protocol: TCP
      name: http
    - port: 443
      targetPort: 443
      protocol: TCP
      name: https
'''

It requires "serviceAccount" with the right set of permissions. We can create a service account with the correct "roles", "clusterRoles" and "roleBindings".
'''
apiVersion: v1
kind: ServiceAccount
metadata:
  name: nginx-ingress-serviceaccount
'''
In Kubernetes, a ServiceAccount is an object that represents an identity used by a pod or a container running inside the cluster to interact with the Kubernetes API server or other services. ServiceAccounts are used to authenticate and authorize requests to the API server, as well as to manage permissions and access control.

When a pod or a container running inside the Kubernetes cluster makes a request to the API server, it can use the credentials associated with its ServiceAccount to authenticate itself. The Kubernetes API server then verifies the ServiceAccount's credentials and authorizes the request based on the permissions granted to the ServiceAccount.

ServiceAccounts can be created using the Kubernetes API or through configuration files, and can be associated with specific namespaces or the entire cluster. By default, each namespace in a Kubernetes cluster has its own default ServiceAccount, which is used by pods or containers running in that namespace unless otherwise specified.

ServiceAccounts play an important role in securing and managing access to resources in a Kubernetes cluster. They provide a mechanism for authenticating and authorizing requests to the API server, as well as managing permissions and access control for individual pods or containers running inside the cluster.


we can create an Ingress resource from the imperative way like this:-

Format - kubectl create ingress <ingress-name> --rule="host/path=service:port"

Example - kubectl create ingress ingress-test --rule="wear.my-online-store.com/wear*=wear-service:80"

Find more information and examples in the below reference link:-

https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-ingress-em-

References:-

https://kubernetes.io/docs/concepts/services-networking/ingress


