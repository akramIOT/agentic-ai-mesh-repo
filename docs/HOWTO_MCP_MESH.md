# MCP Gateway + Istio Ambient + SPIRE — How-To

## Local quickstart (minikube)

1. Start minikube:
```bash
minikube start --driver=docker --memory=8g --cpus=4
```

2. Enable ingress:
```bash
minikube addons enable ingress
```

3. Install Istio:
```bash
istioctl install --set profile=minimal
# or ambient: istioctl install --set profile=ambient
```

4. (Optional) Deploy SPIRE demo or skip for PoC.

5. Helm install charts:
```bash
helm install mcp-gateway charts/mcp-gateway --create-namespace -n demo
helm install mcp-tool charts/mcp-gateway --create-namespace -n demo
```

6. Port-forward and test:
```bash
kubectl -n demo port-forward svc/mcp-gateway 8080:8080 &
python3 examples/python/agent_client.py
```

## Production (EKS with Terraform)

Follow terraform/eks to provision EKS, configure kubectl, install Istio ambient, deploy SPIRE, and apply Istio AuthorizationPolicy/RequestAuthentication resources to require mTLS and JWT validation.
