import threading

def thread_task():
    print(f"Поток {threading.current_thread().name} выполняется")

threads = []
for i in range(3):
    t = threading.Thread(target=thread_task, name=f"MyThread-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()