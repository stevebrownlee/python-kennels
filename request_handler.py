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

        elif resource == "customers":
            if id is not None:
                response = get_single_customer(id)

                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = { "message": f"Animal {id} is out playing right now" }
            else:
                self._set_headers(200)
                response = get_all_customers()


        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        '''Reads post request body'''
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        created_resource = None

        # Add a new animal to the list
        if resource == "animals":
            created_resource = create_animal(post_body)
        elif resource == "locations":
            if "name" in post_body and "address" in post_body:
                self._set_headers(201)
                created_resource = create_location(post_body)
            else:
                self._set_headers(400)
                created_resource = {
                    "message": f'{"name is required" if "name" not in post_body else ""} {"address is required" if "address" not in post_body else ""}'
                }

        # Encode the new animal and send in response
        self.wfile.write(json.dumps(created_resource).encode())

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

        response = ""

        # Delete a single animal from the list
        if resource == "animals":
            self._set_headers(204)
            delete_animal(id)

        elif resource == "customers":
            self._set_headers(405)
            response = {
                "message": "Deleting customers requires contacting the company directly."
            }


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