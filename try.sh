docker build -t dijure/"$1":0.0.1 -f "Dockerfile-$1" .
docker run -d -it -p 80:8080 dijure/test:v1
curl -s $(minikube ip):80
docker kill $(docker ps --filter label=scenario=python-pipelining --format "{{.ID}}")
