from http import client
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from repository import all, delete, create, update, retrieve


class HandleRequests(BaseHTTPRequestHandler):

    def do_GET(self):
        response = None
        (resource, id) = self.parse_url(self.path)

        if id is not None:
            response = retrieve(resource, id)

            if response is not None:
                self._set_headers(200)
            else:
                self._set_headers(404)
                response = ''
        else:
            self._set_headers(200)
            response = all(resource)

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        '''Reads post request body'''
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        created_resource = None
        create(resource, post_body)

        self.wfile.write(json.dumps(created_resource).encode())

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        success = False
        success = update(resource, id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):

        (resource, id) = self.parse_url(self.path)

        response = ""

        if resource == "customers":
            self._set_headers(405)
            response = {
                "message": "Deleting customers requires contacting the company directly."
            }
        else:
            delete(resource, id)

        # Encode the new animal and send in response
        self.wfile.write(json.dumps(response).encode())

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
