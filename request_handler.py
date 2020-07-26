from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.path == "/animals":
            response = f"{get_all_animals(self)}"
            self.wfile.write(response.encode())

    def do_POST(self):
        '''Reads post request body'''
        self._set_headers()
        print(self.path)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = f"received post request:<br>{post_body}"
        self.wfile.write(response.encode())

    def do_PUT(self):
        self.do_POST()


host = ''
port = 8088
HTTPServer((host, port), HandleRequests).serve_forever()
