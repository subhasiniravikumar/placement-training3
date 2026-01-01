import threading
import time

buffer = []
lock = threading.Lock()

def producer():
    for i in range(5):
        time.sleep(1)
        lock.acquire()
        buffer.append(i)
        print("Produced:", i)
        lock.release()

def consumer():
    for _ in range(5):
        time.sleep(2)
        lock.acquire()
        if buffer:
            print("Consumed:", buffer.pop(0))
        lock.release()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()
