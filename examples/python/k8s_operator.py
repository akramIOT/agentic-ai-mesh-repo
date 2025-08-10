# examples/python/k8s_operator.py
from kubernetes import client, config

# For local testing use config.load_kube_config()
# In-cluster use: config.load_incluster_config()
try:
    config.load_incluster_config()
except Exception:
    config.load_kube_config()

apps = client.AppsV1Api()

def scale_deployment(name, namespace, replicas):
    body = {'spec': {'replicas': replicas}}
    resp = apps.patch_namespaced_deployment_scale(name, namespace, body)
    print('Scaled:', resp.metadata.name, '->', resp.spec.replicas)

if __name__ == '__main__':
    scale_deployment('agent-orchestrator', 'default', 3)
