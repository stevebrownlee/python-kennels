from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals, get_single_animal


def parse_url(path):
    path_params = path.split("/")
    resource = path_params[1]
    id = None

    try:
        id = int(path_params[2])
    except IndexError:
        # No route parameter exists
        pass

    return (resource, id)


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        (resource, id) = parse_url(self.path)

        if resource == "animals":
            if id is not None:
                response = f"{get_single_animal(id)}"

            else:
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


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()
