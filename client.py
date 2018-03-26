import requests
import time


t0 = time.time()
response = requests.get("http://localhost:8080/c/algorithm1").json()
t = time.time() - t0

print("Pi:", response["pi"])
print("Server time:", response["t"])
print("Total time:", t)

