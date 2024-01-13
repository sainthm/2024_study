# thread_test.py

import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"working: {i + 1}")

print("Start")

threads = []
for i in range(5):
    # long_task()
    t = threading.Thread(target=long_task) # Make thread
    threads.append(t)

for t in threads:
    t.start() # Start thread

print("End")