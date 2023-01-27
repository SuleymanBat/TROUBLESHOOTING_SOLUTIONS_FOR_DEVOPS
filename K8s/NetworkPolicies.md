##### WARMUP 1:

###### How many "Network Policies" do you see in the environment? We have deployed few applications, services and network policies.Inspect the environment.

Run the command: 

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
> ``kubectl describe networkpolicy and look under the Policy Types section.``

##### WARMUP 4:
###### What is the impact of the rule configured on this Network Policy?
















##### WARMUP 5:
##### Perform a connectivity test using the User Interface in these Applications to access the "payroll-service" at port "8080".






















##### WARMUP 6:
##### Perform a connectivity test using the User Interface of the internal Application to access the "external-service" at port "8080".


























##### WARMUP 7:
##### Create a network policy to allow traffic from the "Internal" application only to the "payroll-service" and "db-service".Use the spec given on the below.

> ``PolicyName: internal-policy``

> ``PolicyType: Egress``

> ``EgressAllow: payroll``

> ``PayrollPort: 8080``

> ``Egress Allow: mysql``

> ``MySQL Port: 3306``



