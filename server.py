import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "www.procurabusiness.com"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Strip /www.procurabusiness.com/ if it's in the path
        if self.path.startswith('/www.procurabusiness.com/'):
            self.path = self.path[len('/www.procurabusiness.com'):]
            
        # Map extensionless paths to .html
        if not self.path.endswith('/') and '.' not in self.path:
            if os.path.exists(os.path.join(DIRECTORY, self.path.lstrip('/') + '.html')):
                self.path += '.html'
        
        try:
            return super().do_GET()
        except ConnectionError:
            pass # Ignore connection errors when client disconnects

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

with ThreadingHTTPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

