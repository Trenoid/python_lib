import os
import threading
from queue import Queue


class FileSearcher:
    def __init__(self, max_threads=4):
        self.queue = Queue()
        self.results = []
        self.lock = threading.Lock()
        self.max_threads = max_threads

    def search(self, pattern, directories):
        for d in directories:
            self.queue.put(d)

        for _ in range(self.max_threads):
            t = threading.Thread(target=self._worker, args=(pattern,))
            t.start()

        self.queue.join()
        return self.results

    def _worker(self, pattern):
        while True:
            try:
                directory = self.queue.get_nowait()
            except:
                return

            for root, _, files in os.walk(directory):
                for file in files:
                    if pattern in file:
                        with self.lock:
                            self.results.append(os.path.join(root, file))
            self.queue.task_done()


# Использование:
searcher = FileSearcher(max_threads=4)
results = searcher.search(".py", ["/", "/"])
print(results)