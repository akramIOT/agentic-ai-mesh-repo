# Minikube Quickstart (Agentic AI Service Mesh)

1. Start minikube:
```bash
minikube start --driver=docker --memory=8g --cpus=4
```

2. Enable ingress (optional):
```bash
minikube addons enable ingress
```

3. Install Istio (minimal/ambient):
```bash
istioctl install --set profile=minimal
# or for ambient: istioctl install --set profile=ambient
```

4. (Optional) Deploy a simple SPIRE demo or skip and use JWT auth for proof-of-concept.

5. Install Helm charts:
```bash
helm install mcp-gateway charts/mcp-gateway --create-namespace -n demo
helm install mcp-tool charts/mcp-gateway --create-namespace -n demo
```

6. Port-forward and test:
```bash
kubectl -n demo port-forward svc/mcp-gateway 8080:8080 &
python3 examples/python/agent_client.py
```
