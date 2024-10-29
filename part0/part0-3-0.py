import threading

def foo():
    print("hello world")

threads = []

for i in range(5):
    thread_temp = threading.Thread(target  = foo)
    threads.append(thread_temp)

for t in threads:#manual starting
    t.start()

for t in threads:
    t.join()
