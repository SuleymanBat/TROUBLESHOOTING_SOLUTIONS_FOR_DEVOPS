# WARMUP-10

##### A NEW USER ANTON JOINED THE TEAM. HE WILL BE CONCANTRATE ON THE NODES IN THE CLUSTER. CREATE THE REQUIRED "CLUSTERROLES AND CLUSTERROLEBINDINGS" SO SHE GETS ACCESS TO THE NODES.

Use the command "kubectl create" to create a "clusterrole and clusterrolebinding" for user "anton" to grant access to the nodes.
After that test the access using the command "kubectl auth can-i list nodes --as michelle".

> '''kubectl create clusterrole anton --verb=get,list,watch --resource=nodes'''

> '''kubectl auth can-i list nodes --as anton'''

> ''' kubectl create clusterrolebinding anton --clusterrole=anton --user=anton'''

> '''kubectl auth can-i list nodes --as anton'''
At the end you must see the result "yes"

# WARMUP-11

###### ANTON's responsibilities are growing and now he will be responsible for storage as well. Create the required "ClusterRoles and ClusterRoleBindings" to allow him access to Storage.Get the API groups and resource names from command "kubectl api-resources". Use the given spec:


ClusterRole: storage-admin

Resource: persistentvolumes

Resource: storageclasses

ClusterRoleBinding: anton-storage-admin

ClusterRoleBinding Subject: anton

ClusterRoleBinding Role: storage-admin

> '''k create clusterrole  storage-admin --resource=persistentvolumes,storageclasses --verb=get,list,watch,create'''

> ``k describe clusterrole storage-admin``

> ``k get clusterrole storage-admin -o yaml``

>  ``k create clusterrolebinding anton-storage-admin --user=anton --clusterrole=storage-admin``

> ``k describe clusterrolebinding anton-storage-admin``

> ``k --as anton get storageclasses``