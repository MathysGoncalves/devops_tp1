---
title: TP1 DevOps - Docker
author: Mathys Goncalves
geometry: margin=10cm
---

# TP1 DevOps - Docker
<div style="text-align: right"> Mathys Goncalves - BDIA </div>
</br>

The objective is to create a python script returning the temperature of the place provided thanks to the coordinates (Lat, Lon).
The user will have to provide their own API Key which will not be stored by the application.

</br>

## Dockerization Process
</br>

We have chosen a lightweight version of the Python image which is *python:alpine3.16*.
In our Dockerfile, we import this image and define our python script which is *weather.py*.
Note that here it is necessary to indicate a file *requirements.txt*. The python library *pipreqs* was used to simply generate it beforehand.

```dockerfile
FROM python:alpine3.16

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "weather.py"]
```
</br>

To create the container, it is first necessary to start Docker, then to build.
weather being the name followed by the version (0.0.1).

```ps
systemctl start docker 
docker build . -t weather:0.0.1 
```
</br>

We can now verify that the container works:

```ps
docker run --env LAT="5.902785" --env LONG="102.754175" --env API_KEY="d69124de3c4d3d37c00bcbea674da2d6" weather:0.0.1
```
</br>

We then want to make it available in Docker Hub:

```ps
docker tag weather:0.0.3 mathysgoncalves/tp1-devops-mathys_goncalves:0.0.3
docker push mathysgoncalves/tp1-devops-mathys_goncalves:0.0.3 

[Output]
    The push refers to repository [docker.io/mathysgoncalves/tp1-devops-mathys_goncalves]
    dbda11960a93: Pushed 
    d39899158b2d: Pushed 
    66e199943e84: Pushed 
    ed551d741cb0: Pushed 
    0347066a1a00: Pushed 
    5bb1a595ed81: Pushed 
    27f7e4620f8d: Pushed 
    09c126bb3acd: Pushed 
    24302eb7d908: Pushed 
    0.0.3: digest: sha256:*** size: 2199
```
</br>

We can now test the application:
```ps
docker run --env LAT="5.902785" --env LONG="102.754175" --env API_KEY="d69124de3c4d3d37c00bcbea674da2d6" mathysgoncalves/tp1-devops-mathys_goncalves:0.0.3
```
</br>

## Extra
</br>

Check for vulnerability :

```ps
trivy image mathysgoncalves/tp1-devops-mathys_goncalves:0.0.3 

[Output]
    2022-06-03T11:30:18.983+0200    INFO    Detected OS: alpine
    2022-06-03T11:30:18.983+0200    INFO    This OS version is not on the EOL list: alpine 3.16
    2022-06-03T11:30:18.983+0200    INFO    Detecting Alpine vulnerabilities...
    2022-06-03T11:30:18.985+0200    INFO    Number of language-specific files: 1
    2022-06-03T11:30:18.985+0200    INFO    Detecting python-pkg vulnerabilities...

    mathysgoncalves/tp1-devops-mathys_goncalves:0.0.3 (alpine 3.16.0)
    =================================================================
    Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)


    Python (python-pkg)
    ===================
    Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)
```
</br>

Check for version 

```ps
docker run --rm -i hadolint/hadolint < Dockerfile

[Output]
    Unable to find image 'hadolint/hadolint:latest' locally
    latest: Pulling from hadolint/hadolint
    6449f89468e7: Pull complete 
    Digest: sha256:93f0afd12c3be5d732227c0226dd8e7bb84f79319a773d7f8519e55f958ba415
    Status: Downloaded newer image for hadolint/hadolint:latest

```
