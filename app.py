from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from GitHub Actions + Kubernetes!")

server = HTTPServer(("0.0.0.0", 8080), handler)
server.serve_forever()