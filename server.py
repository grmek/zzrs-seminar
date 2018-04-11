import http.server
import socketserver
import subprocess
import time
import json


HOST = ""
PORT = 8080
CMD = {
    "/c/algorithm1": "algorithms/algorithm1.o 24473399",
    "/c/algorithm2": "algorithms/algorithm2.o 2",
    "/python/algorithm1": "python3 algorithms/algorithm1.py 24473399",
    "/python/algorithm2": "python3 algorithms/algorithm2.py 2"
}


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            result = "<!DOCTYPE html>\n<html>\n<body>\n<h2>Available functionalities:</h2>\n<ul>\n"
            for path in sorted(CMD.keys()):
                result += "  <li><a href=\"" + path + "\">" + path + "</a></li>\n"
            result += "</ul>\n</body>\n</html>\n"
            self.wfile.write(bytes(result, "utf-8"))
        elif self.path in CMD:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            t0 = time.time()
            pi = float(subprocess.check_output(CMD[self.path], shell=True).decode("utf-8"))
            t = time.time() - t0
            result = {"pi": pi, "t": t}
            self.wfile.write(bytes(json.dumps(result), "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            result = "<!DOCTYPE html>\n<html>\n<body>\n<h1>404 Not Found</h1>\n</body>\n</html>\n"
            self.wfile.write(bytes(result, "utf-8"))


httpd = socketserver.TCPServer((HOST, PORT), Handler)
print('Serving started.')
httpd.serve_forever()

