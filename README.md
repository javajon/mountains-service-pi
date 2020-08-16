# Python Microservice in Distilled Containers

This is a small example microservice based in Python. It demonstrates some basic REST based commands that maintain a list of mountain information. The REST calls setup basic CRUD instructions to create, read, update, and delete information about mountains. Why mountains? It's arbitrary and generic. This service does not connect to a database, but provides a skeleton where that certainly could be added as a teaching exercise. The purpose is to explore a basic microservice that servers JSON REST and is packaged into a container. The container is intended to be used for teaching about Kubernetes in a Katacoda scenario. For a better understanding of this project, follow this [Katacoda scenario](https://katacoda.com/javajon/courses/kubernetes-pipelines/python).

There are several web frameworks in Python to choose from, and for this example the FastAPI with uvicorn were chosen.

More could be added to this skeleton by following this [helpful example from Paurakh Sharma Humagain](https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc#creating-simple-rest).

The slimming of the Dockerfile was inspired by two projects.

1. The creator of [FastAPI](https://github.com/tiangolo/fastapi), [Sebastián Ramírez](https://github.com/tiangolo), also created a project with efficient [base containers for FastAPI](https://github.com/tiangolo/uvicorn-gunicorn-docker).

2. [Wojtek @suda Siudzinski](https://suda.pl/) blog on [Production-ready Django 3 ASGI Docker image](https://suda.pl/deploying-django-3-asgi/) and [accompanying source code](https://github.com/stefanitsky/cookiecutter-django-minimal).

## Running Instructions

There are a few Dockerfiles that will package the Python microservice differently. They all can be run using the ./try.sh script.

`./try.sh bloated`
`./try.sh slim`
`./try.sh alpine`

## References

[How to Build Slim Docker Images Fast](https://towardsdatascience.com/how-to-build-slim-docker-images-fast-ecc246d7f4a7)

[Production-ready Django 3 ASGI Docker image](https://suda.pl/deploying-django-3-asgi/)

[Microservice in Python using FastAPI](https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc#installing-docker)

[FastAPI](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)

[FastAPI Containers](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)

[Example Dockerfile](https://github.com/stefanitsky/cookiecutter-django-minimal/blob/cc08d4e593b163ebbb002890d07fa3d3c084ee70/%7B%7B%20cookiecutter.project_slug%20%7D%7D/Dockerfile)

[Example Dockerfile](https://github.com/klasrak/eventex/blob/eafa1cdd12e8d2cd0b9da56a908e61e825ca41a1/Dockerfile)
