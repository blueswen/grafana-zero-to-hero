# kKube Prometheus Stack

<https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack>

1. Kubernetes with k3s/k3d
2. kube-prometheus-stack with helm

## Kubernetes

### k3s

<https://k3s.io/>

```bash
curl -sfL https://get.k3s.io | sh - 
# Check for Ready node, takes ~30 seconds 
sudo k3s kubectl get node 
```

### k3d

<https://k3d.io/>

```bash
k3d cluster create --config k3d/conf.yaml
# Check for Ready node, takes ~30 seconds
kubectl get node

# Stop
k3d cluster stop kube-prom-stack-lab

# Teardown
k3d cluster delete kube-prom-stack-lab
```

## kube-prometheus-stack

### Install

```bash
helm add repo prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm upgrade --install prometheus-community prometheus-community/kube-prometheus-stack --version 70.1.1 --namespace monitoring --create-namespace -f values.yaml
```

### Usage

```bash
# Port forward Prometheus
kubectl port-forward -n monitoring svc/prometheus-community-kube-prometheus 9090:9090

# Retrieve Grafana password
kubectl get secret prometheus-community-grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
# Port forward Grafana
kubectl port-forward -n monitoring svc/prometheus-community-grafana 3000:80
```

## Application Monitoring

```bash
# Deploy application
kubectl apply -f app.yaml

# Port forward application
kubectl port-forward svc/fastapi 8000:8000
```
