# About the Repo
This repo is part of the LLMOps course by Manifold AI Learning,
Course link - https://www.manifoldailearning.in/courses/LLMOps-with-ChatGPT-Deploy-on-Production-65cb265ae4b086660d2836ae

Reach the Instructor at - https://www.linkedin.com/in/nachiketh-murthy/

For any support reach out to : support@manifoldailearning.in

# Help on FAST API

```
pip install "fastapi[all]"

uvicorn main:app --reload
```

# Test with Postman

URL - http://127.0.0.1:80/response
(POST)

```json
{
  "text": "Who is the hero of the story"
}

```

# Docker Commands

```
docker build -t chatgpt-project1 .
docker run -d -p 8080:80 chatgpt-project1
docker tag chatgpt-project1 yourusername/chatgpt-project1
docker push yourusername/chatgpt-project1
```

# Kubernetes Code

```
kubectl create secret generic openai-secret --from-literal=API_KEY=<api-key>
```