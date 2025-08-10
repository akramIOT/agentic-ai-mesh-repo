# examples/python/mcp_server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MCPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(length).decode('utf-8')
        data = json.loads(body)
        # Expecting {"jsonrpc":"2.0","method":"invoke","params":{...},"id":1}
        method = data.get('method')
        params = data.get('params', {})
        # Simple echo tool -> real tools would validate, authenticate, and sanitize
        result = {"echo": params}
        response = {
            "jsonrpc": "2.0",
            "result": result,
            "id": data.get('id')
        }
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 9090), MCPHandler)
    print('MCP Tool Server running on 0.0.0.0:9090')
    server.serve_forever()
