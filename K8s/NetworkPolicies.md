##### WARMUP 1:

###### How many "Network Policies" do you see in the environment? We have deployed few applications, services and network policies.Inspect the environment.

Run the command: 

> ``k get pods``

> ``k get service``

> ``kubectl get networkpolicy or kubectl get netpol``

##### WARMUP 2:
###### Which pod is the "NetworkPolicy" applied on?

Use the command;

> ``kubectl get netpol``

 and look under the Pod Selector column.

 After getting the labels, identify the correct pod name by their labels.

Run the command: 

> ``kubectl get po --show-labels | grep name=payroll``

#### WARMUP 3:
###### What type of traffic is the Network Policy configured to handle?

Run the command: 
> ``kubectl describe networkpolicy and look under the Policy Types section.`

##### WARMUP 4:
###### What is the impact of the rule configured on this Network Policy?

Traffic From Internal to Payroll POD is allowed

##### WARMUP 5:
##### Create a network policy to allow traffic from the "Internal" application only to the "payroll-service" and "db-service".Use the spec given on the below.

> ``PolicyName: internal-policy``

> ``PolicyType: Egress``

> ``EgressAllow: payroll``

> ``PayrollPort: 8080``

> ``Egress Allow: mysql``

> ``MySQL Port: 3306``

We want to block "internal" apps access to everything else except for the "payroll service" and "DataBase" service.This is what we want to achieve. We have to create an "internal-policy".And we have to associate it with the "internal pod". So that's the "pod specification". We're gonna configure egress traffic. We're gonna block everything except for the egress traffic to both of these. Let' s go to K8s documentation and look for "network policies".Let's find a template to start with in the documentaation page.Before Copy paste the template from documentation let's create a file called "internalpolicy.yaml" with using vim editör. Then paste the template inside .yaml file.And change "policyName" like that;

````
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: internal-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      name: internal
  policyTypes:
  - Egress
  - Ingress
  ingress:
    - {}
  egress:
  - to:
    - podSelector:
        matchLabels:
          name: mysql
    ports:
    - protocol: TCP
      port: 3306

  - to:
    - podSelector:
        matchLabels:
          name: payroll
    ports:
    - protocol: TCP
      port: 8080

  - ports:
    - port: 53
      protocol: UDP
    - port: 53
      protocol: TCP
````

Note: We have also allowed Egress traffic to TCP and UDP port. This has been added to ensure that the internal DNS resolution works from the internal pod. Remember: The kube-dns service is exposed on port 53:

> `` k create -f internalpolicy.yaml``

> ``k describe netpol internal-policy"

> ``kubectl get svc -n kube-system ``