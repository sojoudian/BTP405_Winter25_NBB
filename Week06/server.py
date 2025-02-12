from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# In-memory storage:
data_store = []

class SimleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
            data_store.append(data)
            
            # Response with success message
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"message": "Data stored successfully!", "data": data}
            self.wfile.write(json.dumps(response).encode())
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "invalid JSON format"}).encode())
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')  
        self.end_headers()
        self.wfile.write(json.dumps({"stored_data": data_store}).encode())

def run_Server():
    server_address = ('', "8081")
    httpd = HTTPServer(server_address, SimleHTTPRequestHandler)
    print('Starting HTTP server on port  8081')
    httpd.serve_forever()

if __name__ == '__main__':
    run_Server()