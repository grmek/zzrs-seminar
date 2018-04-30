import sys
import threading
import requests
import time


def send_request_and_save_result(idx):
    print("Sending request " + str(idx) + " ...")
    try:
        t0 = time.time()
        response = requests.get(url).json()
        t = time.time() - t0 - response["t"]
    except:
        print("ERROR: No response from server (request " + str(idx) + ").")
        return
    write_lock.acquire()
    with open(file_name, "a") as f:
        f.write("%d\t%.9f\t%.9f\t%.9f\t%.9f\n" % (idx, t0, response["pi"], response["t"], t))
    write_lock.release()


url = sys.argv[1]
file_name = "data/" + sys.argv[2]

with open(file_name, "w") as f:
    f.write("idx\ttimestamp\tpi\tt2\tt1+t3\n")

write_lock = threading.Lock()

t = time.time()
for i in range(100):
    threading.Thread(target=send_request_and_save_result, args=(i,)).start()
    t += 3
    while time.time() < t:
        pass
for i in range(100,250):
    threading.Thread(target=send_request_and_save_result, args=(i,)).start()
    t += 2
    while time.time() < t:
        pass
for i in range(250,550):
    threading.Thread(target=send_request_and_save_result, args=(i,)).start()
    t += 1
    while time.time() < t:
        pass
for i in range(550,1150):
    threading.Thread(target=send_request_and_save_result, args=(i,)).start()
    t += 0.5
    while time.time() < t:
        pass
