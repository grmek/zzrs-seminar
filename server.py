import http.server
import socketserver
import subprocess
import time
import json


HOSTNAME = "localhost"
PORT = 8080
CMD = {
    "/c/algorithm1": "algorithms/algorithm1.o 10000",
    "/c/algorithm2": "algorithms/algorithm2.o 10000",
    "/python/algorithm1": "python algorithms/algorithm1.py 10000",
    "/python/algorithm2": "python algorithms/algorithm2.py 10000"
}


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            result = "<!DOCTYPE html>\n<html>\n<body>\n<h2>Available functionalities:</h2>\n<ul>\n"
            for path in CMD.keys():
                result += "  <li><a href=\"" + path + "\">" + path + "</a></li>\n"
            result += "</ul>\n</body>\n</html>\n"
            self.wfile.write(bytes(result, "utf-8"))
        elif self.path in CMD:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            t0 = time.time()
            pi = subprocess.check_output(CMD[self.path], shell=True).decode("utf-8")
            t = time.time() - t0
            result = {"pi": pi, "t": t}
            self.wfile.write(bytes(json.dumps(result), "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            result = "<!DOCTYPE html>\n<html>\n<body>\n<h1>404 Not Found</h1>\n</body>\n</html>"
            self.wfile.write(bytes(result, "utf-8"))


with socketserver.TCPServer((HOSTNAME, PORT), Handler) as httpd:
    print('Serving started.')
    httpd.serve_forever()

