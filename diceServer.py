"""
some descriptive text
Author: M. Blank
Disclaimer: Not safe, developed for a very specific and private use only. Use at YOUR OWN RISK only!
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class diceRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        # new POST request received, read content and extract necessary parameters
        requestLength = int(self.headers['Content-Length'])
        rawBody = self.rfile.read(requestLength)
        #print("Request body: " + rawBody.decode('utf-8'))
        body = parse_qs(rawBody.decode('utf-8'), encoding='utf-8')
        #print(body)

        # Print output for manual request handling
        print("\n--------------------------------------")
        print("POST request received! Request path: " + self.path)
        print("Number of requested dice rolls: " + body['numdice'][0])
        print(body['subject'][0])
        self._set_response()
        dice = input()
        self.wfile.write("your dice are: {}<p>".format(dice).encode('utf-8'))

    def do_GET(self):
        print("GET request received! Request path: " + self.path)
        self._set_response()
        self.wfile.write(b"Local dice server seems to be up and running!")
        self.wfile.write(b"If you expect anything else here you clearly don't have a very good understanding of what you are doing ;)")


def run(server_class=HTTPServer, handler_class=diceRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()