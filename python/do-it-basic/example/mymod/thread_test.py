# thread_test.py

import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"working: {i + 1}")

print("Start")

for i in range(5):
    long_task()

print("End")