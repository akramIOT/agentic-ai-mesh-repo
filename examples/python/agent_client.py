# examples/python/agent_client.py
import requests
import json

MCP_GATEWAY = 'http://mcp-gateway.demo.svc.cluster.local:8080'

def call_tool(tool_name, payload):
    req = {
        'jsonrpc': '2.0',
        'method': 'invoke',
        'params': {'tool': tool_name, 'input': payload},
        'id': 1
    }
    r = requests.post(MCP_GATEWAY, json=req, timeout=10)
    r.raise_for_status()
    return r.json()

if __name__ == '__main__':
    resp = call_tool('echo', {'text': 'hello from agent'})
    print('Tool response:', json.dumps(resp, indent=2))
