## Which namespace is the Ingress Controller deployed in?

Use the command 

>``kubectl get all -A``

 and identify the namespace of Ingress Controller.

## What is the name of the Ingress Controller Deployment?

Use the command 

>``kubectl get deploy -A ``

or 

>``kubectl get deploy --all-namespaces``

 and identify the name of Ingress Controller.

## Which namespace are the applications deployed in?

Run the command: 

>``kubectl get po -A``

 and identify the namespaces of deployed applications.

## How many applications are deployed in the app-space namespace? Count the number of deployments in this namespace.

Run the command: 

>``kubectl get deploy --namespace app-space``

 and count the number of deployments.

## Which namespace is the Ingress Resource deployed in?

 k get ingress -A

## What is the name of the Ingress Resource?

Run the command: 

>``kubectl get ingress --all-namespaces``

 and identify the name of Ingress Resource.

## What is the Host configured on the Ingress Resource? The host entry defines the domain name that users use to reach the application like www.google.com

Run the command: 

>``kubectl describe ingress --namespace app-space``

 and look at Host under the Rules section.

## What backend is the /wear path on the Ingress configured with?
Run the command: 

>``kubectl describe ingress --namespace app-space``

 and look under the Rules section.

## At what path is the video streaming application made available on the Ingress?

Run the command: 

>``kubectl describe ingress --namespace app-space``

 and look under the Rules section.

## If the requirement does not match any of the configured paths what service are the requests forwarded to?

Run the command: 

>``kubectl describe ingress --namespace app-space``

 and look at the Default backend field.

## You are requested to change the URLs at which the applications are made available.Make the video application available at /stream.

Run the command: 

>``kubectl edit ingress --namespace app-space``

 and change the path to the video streaming application to /stream.

Solution manifest file to change the path to the video streaming application to /stream as follows:

'''
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
  name: ingress-wear-watch
  namespace: app-space
spec:
  rules:
  - http:
      paths:
      - backend:
          service:
            name: wear-service
            port: 
              number: 8080
        path: /wear
        pathType: Prefix
      - backend:
          service:
            name: video-service
            port: 
              number: 8080
        path: /stream
        pathType: Prefix
'''

## You are requested to add a new path to your ingress to make the food delivery application available to your customers.Make the new application available at /eat.

Run the command: 

>``kubectl edit ingress --namespace app-space``

 and add a new Path entry for the new service.


Solution manifest file to add a new path to our ingress service to make the application available at /eat as follows:

'''
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
  name: ingress-wear-watch
  namespace: app-space
spec:
  rules:
  - http:
      paths:
      - backend:
          service:
            name: wear-service
            port: 
              number: 8080
        path: /wear
        pathType: Prefix
      - backend:
          service:
            name: video-service
            port: 
              number: 8080
        path: /stream
        pathType: Prefix
      - backend:
          service:
            name: food-service
            port: 
              number: 8080
        path: /eat
        pathType: Prefix
'''

View the Food delivery application using the /eat URL in your browser.

## A new payment service has been introduced. Since it is critical, the new application is deployed in its own namespace.Identify the namespace in which the new application is deployed.

Run the command: 

>``kubectl get deploy --all-namespaces``

 and inspect the newly created namespace and deployment.

## What is the name of the deployment of the new application?

Run the command: 

>``kubectl get deploy --all-namespaces``

 and identify the new deployment of the payment application.

## You are requested to make the new application available at /pay.Identify and implement the best approach to making this application available on the ingress controller and test to make sure its working. Look into annotations: rewrite-target as well.

Create a new Ingress for the new pay application in the critical-space namespace.
Use the command 

>``kubectl get svc -n critical-space``

 to know the service and port details.


Solution manifest file to create a new ingress service to make the application available at /pay as follows:
'''
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: test-ingress
  namespace: critical-space
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
spec:
  rules:
  - http:
      paths:
      - path: /pay
        pathType: Prefix
        backend:
          service:
           name: pay-service
           port:
            number: 8282
'''

>``k create ingress test-ingress -n critical-space --rule="/pay=pay-service:8282"

>``k get ingress -n critical-space``

>`` k describe ingress -n critical-space``

>``k get pods -n critical-space``

>``k logs webapp-pay<name> -n critical-space``

>``k edit ingress test-ingress -n critical-space``
