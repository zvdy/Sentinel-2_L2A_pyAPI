# Sentinel-2 Image Processing API

## Description

This is a Python backend that uses FastAPI to expose a REST API. 

The API works with Sentinel-2 satellite images. It has two endpoints: 

- `/attributes`: Returns the attributes of the image (e.g. width, height, bands, etc.)

- `/thumbnail`: Returns a thumbnail of the image at a given resolution (e.g. 200x200)

The application uses Rasterio to read the image and Pillow to create the thumbnail.

## Installation

This guide explains how to install and deploy the `Sentinel-2_L2A_pyAPI` application using Docker and Kubernetes.

### Prerequisites

Before you begin, you'll need the following:

- Docker installed on your machine
- A Kubernetes cluster (e.g. Minikube) installed on your machine
- kubectl installed on your machine
- Python 3.9 or higher installed on your machine
- pip installed on your machine
- git installed on your machine
- Docker hub account (or other Docker registry account)



### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/zvdy/Sentinel-2_L2A_pyAPI.git
cd Sentinel-2_L2A_pyAPI
```



### Step 2: Install the requirements and virtual environment


```bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```


### Step 3: Build or pull the docker image

```bash
docker pull zvdy/py-backend:tag
``` 

### Step 4: Run minikube

```bash
minikube start
```

### Step 5: Run the deployment

```bash
kubectl apply -f kubernetes/deployment.yaml
```

### Step 6: Run the service

``` bash
kubectl apply -f kubernetes/service.yaml
```

### Step 7: Expose the external IP 

> Or use nodePort if you don't have a load balancer _(not recommended for production)_

```bash
minikube tunnel
```

### Step 8: Check the external IP

```bash
kubectl get service
```

### Step 9: Test the deployed app

![image](/img/img.png)


## Tests

### /attributes

```bash 
curl -X POST -F "image_file=@S2L2A_2022-06-09.tiff" http://localhost:8000/attributes
```


### /thumbnail

```bash 
curl -X POST -F "image_file=@S2L2A_2022-06-09.tiff" -F "target_resolution=200" http://localhost:8000/thumbnail --output output.png
```


## Deployment Manifest

The project has two yaml files, `deployment.yaml` and `service.yaml`. The `deployment.yaml` file contains the deployment manifest, which defines the deployment of the application. The `service.yaml` file contains the service manifest, which defines the service that exposes the application.

## Scaling

To scale the application, you can modify the `spec.replicas` field in the deployment manifest. For example, to scale to 3 replicas, you can run the following command:

```
kubectl scale deployment py-backend --replicas=3
```

## Monitoring

To monitor the application, you can use Kubernetes tools such as `kubectl logs` and `kubectl exec`. You can also use external monitoring tools such as Prometheus and Grafana.

## Considerations

When deploying the application, consider the following:

- Security: Ensure that the container image is secure and that the Kubernetes cluster is properly secured.
- High availability: Consider using multiple replicas and configuring Kubernetes to automatically recover from failures.
- Load balancing: Consider using a load balancer to distribute traffic across multiple replicas.
- Storage: Consider using persistent volumes to store data that needs to persist across container restarts.
- Upgrades: Consider using rolling updates to deploy new versions of the container without downtime.
- Logging: Consider using a logging solution to collect logs from the application.

## References  

- [Kubernetes documentation](https://kubernetes.io/docs/home/)
- [Rasterio documentation](https://rasterio.readthedocs.io/en/latest/)
- [Sentinel2](https://docs.sentinel-hub.com/api/latest/data/sentinel-2-l2a/)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Docker documentation](https://docs.docker.com/)
- [Minikube documentation](https://minikube.sigs.k8s.io/docs/)
- [RGB Composites](https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/composites/)
- [Convert to RGB](https://stackoverflow.com/questions/56760139/convert-16-bit-tiff-image-to-8-bit-rgb)
- [Python multipart](https://andrew-d.github.io/python-multipart/)
- [Numpy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)
- [Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html)
- [Uvicorn](https://www.uvicorn.org/)

## License

This work is licensed under the Creative Commons Attribution-NonCommercial (CC BY-NC) license. 

See [LICENSE](LICENSE) for details.