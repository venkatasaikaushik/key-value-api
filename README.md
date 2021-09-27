# Overview:
This repository helps you in creating a backend service (http API) with the help of "Python" and "Flask" by using "Redis" as a "In-memory key-value store". This repository contains the "Dockerfile" which helps dockerizing the service. It also has the "Manifest files of Kubernetes" which helps in deploying the docker image in Kubernetes. This project has been tested locally in "Minikube" cluster and everything works as expected.

# Requirements:
1. Docker pre-installed on your OS.
2. minikube cluster setup on your OS.

# How to run the project:
1. The file "key_value_api.py" containes the python service which acts as a backend http API and stores key-value pairs in "In-memory key-value store". With the help of "Dockerfile" and the below command, we should first dockerize our python script and generate an image which can be used in Kubernetes.
	**command**: "docker image build -t keyvalueapi ."
2. Once the image is created, we are ready to create a new environment in our Kubernetes cluster with the help of "Namespace". We can do it by running the below command and the file "namespace.yml" in this repo.
	**command**: kubectl apply -f namespace.yml
3. Once the namespace is ready, we are good to setup our service in the new environment of our Kubernetes cluster. We can do it by running below commands and the files in "manifest_files" folder.
	**a**. kubectl apply -f keyvalueapi-deployment-service.yml
	**b**. kubectl apply -f keyvalueapi-ingress.yml
  	**c**. kubectl apply -f redis-deployment-service.yml
4. Once you finish running the above commands, you can check the current pods, deployments, services and ingresses by running the below commands.
	**a**. kubectl get po -n test-env
	**b**. kubectl get deployment -n test-env
	**c**. kubectl get ing -n test-env
	**d**. kubectl get svc -n test-env
5. You can check now the status of pods and the count of desired number of pods will be up and running.
6. Finally we can access our sample api at "http://keyvalueapi.com:32044/" 

# Functionalities of this service:
1. "/get": "http://keyvalueapi.com:32044/get" --> this API call returns all the current present key-value pairs in the In-memory key-value store.
2. "/search": 
	**a**. "prefix": "http://keyvalueapi.com:32044/search?prefix=abc" --> this API call returns all the keys with prefix "abc" in the form of a list.
	**b**. "suffix": "http://keyvalueapi.com:32044/search?suffix=-1" --> this API call returns all the keys with suffix "-1" in the form of a list.
3. "/get/<key>": "http://keyvalueapi.com:32044/get/abc-1" --> this API call returns the value of the key "abc-1".
4. "/set": "curl -X POST -H "Content-Type: application/json" -d '{"test-1":"trash-1"}' http://keyvalueapi.com:32044/set" --> this API call adds a new key-value pair to the existing In-memory key-value store
5. "/delete/<key>": "http://keyvalueapi.com:32044/delete/abc-1"--> this API call deletes the key-value pair with key "abc-1" from the In-memory key-value store.
