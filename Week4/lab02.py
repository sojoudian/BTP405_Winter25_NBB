import http.server
import socketserver

PORT = 8001

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!\n")

httpd = socketserver.TCPServer(("", PORT), MyHandler)
print(f"Server is running at http://localhost:{PORT}")
httpd.serve_forever()
