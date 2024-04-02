# About the Repo

# Docker Commands

```
docker buildx build --platform=linux/amd64 -t manifoldailearning/gpt-project:v1 .
# test locally
# Test with CI CD
docker push manifoldailearning/gpt-project:v1

docker run -d -p 8080:80 manifoldailearning/gpt-project:v1
docker run -p 8080:80 manifoldailearning/gpt-project:v1
```

# Kubernetes Code

```
kubectl create secret generic openai-secret --from-literal=API_KEY=<api-key>
```

# Important Code for Docker

```
docker buildx build --platform=linux/amd64 -t manifoldailearning/gpt-project:v1 .
docker push yourusername/gpt-project:v1

docker run -d -p 8001:80 manifoldailearning/gpt-project:v1
```