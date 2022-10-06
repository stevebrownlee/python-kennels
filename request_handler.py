import json
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from locations.request import get_all_locations
from animals import *
from customers import *
from locations import *


class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        url_components = urlparse(path)
        path_params = url_components.path.strip("/").split("/")
        query_params = []

        if url_components.query != '':
            query_params = url_components.query.split("&")

        resource = path_params[0]
        id = None

        try:
            id = int(path_params[1])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id, query_params)  # This is a tuple

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()


    def do_GET(self):
        self._set_headers(200)

        response = {}
        parsed = self.parse_url(self.path)

        ( resource, id, query_params ) = parsed

        if resource == "animals":
            if id is not None:
                response = f"{get_single_animal(id)}"
            else:
                response = f"{get_all_animals(query_params)}"
        elif resource == "locations":
            if id is not None:
                response = f"{get_single_animal(id)}"
                pass
            else:
                response = f"{get_all_locations()}"
        elif resource == "customers":
            if id is not None:
                response = f"{get_single_customer(id)}"
            else:
                response = f"{get_all_customers()}"
        elif resource == "employees":
            if id is not None:
                response = f"{get_single_customer(id)}"
            else:
                response = f"{get_all_customers()}"


        self.wfile.write(response.encode())

    def do_POST(self):
        '''Reads post request body'''
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id, query_params) = self.parse_url(self.path)

        # Initialize new animal
        new_animal = None

        # Add a new animal to the list
        if resource == "animals":
            new_animal = create_animal(post_body)
        elif resource == "customers":
            new_animal = create_customer(post_body)
        elif resource == "locations":
            new_animal = create_animal(post_body)
        elif resource == "employees":
            new_animal = create_animal(post_body)

        # Encode the new animal and send in response
        self.wfile.write(f"{new_animal}".encode())

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        success = False

        if resource == "animals":
            success = update_animal(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())



    def do_DELETE(self):

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            success = delete_animal(id)   # True or False

            if success:
                self._set_headers(204) # SUCCESS, NO CONTENT
            else:
                self._set_headers(404) # Resource doesn't exist 200, 201, 204, 401, 403, 404, 413, 500

        # Encode the new animal and send in response
        self.wfile.write("".encode())


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()