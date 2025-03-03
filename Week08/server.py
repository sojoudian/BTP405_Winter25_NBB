import http.server
import socketserver

PORT = 9000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving Web Service at http://localhost:{PORT}")
    print(" Press Ctrl+c to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")    
        httpd.server_close()
