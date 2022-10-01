import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal
from views import get_all_locations, get_single_location, create_location, delete_location, update_location
from views import get_all_customers, get_single_customer, create_customer, delete_customer, update_customer
from views import get_all_customers, get_single_customer, create_customer, delete_customer, update_customer


class HandleRequests(BaseHTTPRequestHandler):

    def do_GET(self):
        response = None
        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            if id is not None:
                response = get_single_animal(id)

                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = { "message": f"Animal {id} is out playing right now" }
            else:
                self._set_headers(200)
                response = get_all_animals()

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        '''Reads post request body'''
        self._set_headers(200)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_animal = None

        # Add a new animal to the list
        if resource == "animals":
            new_animal = create_animal(post_body)

        # Encode the new animal and send in response
        self.wfile.write(json.dumps(new_animal).encode())

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
        self._set_no_content_headers()

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            delete_animal(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

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