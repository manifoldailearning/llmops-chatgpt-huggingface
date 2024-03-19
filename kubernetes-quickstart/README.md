# Commands used in the Hands On
```
docker --version
docker pull nginx
docker images
docker run -d -p 8080:80 nginx
docker ps
docker stop <container_id>


docker build -t custom-nginx .
docker tag custom-nginx yourusername/custom-nginx
docker push yourusername/custom-nginx
```

# Commands for Kubernetes

```
kubectl get pods
kubectl apply -f pod.yaml
kubectl describe pod myapp

kubectl apply -f svc-local.yaml
kubectl get svc
kubectl describe svc mysvc

kubectl delete pods --all
kubectl delete svc --all

kubectl api-resources
kebectl get deployments
kubectl apply -f deployment.yaml
kubectl describe deployments

kubectl rollout status deployment


kubectl create configmap app-config --from-literal=DATABASE_URL="mysql://user:password@mysql-server:3306/db_name"

kubectl describe cm app-config 

kubectl exec -it app-pod -- /bin/bash

kubectl create secret generic db-secret --from-literal=DB_PASSWORD=password123


kubectl exec -it db-pod -- /bin/bash
```

# Deployment Object
- self healing
- scaling
- rolling updates

# Deployment Controller
- Process which runs on the Control Plane that monitors the cluster making use all the deployment object are running as per the specification