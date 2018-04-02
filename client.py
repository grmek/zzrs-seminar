import sys
import threading
import requests
import time


def send_request_and_save_result(idx):
    t0 = time.time()
    response = requests.get("http://localhost:8080/c/algorithm1").json()
    t = time.time() - t0
    write_lock.acquire()
    with open(file_name, "a") as f:
        f.write("%d\t%f\t%f\t%f\t%f\n" % (idx, t0, response["pi"], response["t"], t))
    write_lock.release()


url = sys.argv[1]
interval = float(sys.argv[2])
num_requests = int(sys.argv[3])
file_name = "data/" + sys.argv[4]

with open(file_name, "w") as f:
    f.write("idx\ttimestamp\tpi\tt2\tt1+t3\n")

write_lock = threading.Lock()

for i in range(num_requests):
    t0 = time.time()
    threading.Thread(target=send_request_and_save_result, args=(i,)).start()
    while (time.time() - t0) < interval:
        pass

