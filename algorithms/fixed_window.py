import time
from collections import defaultdict
from threading import Lock

class FixedWindowLimiter:

    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(int)
        self.lock = Lock()

    def allow_request(self, client_id):

        current_window = int(time.time() / self.window_seconds)
        key = (client_id, current_window)

        with self.lock:
            if self.requests[key] < self.max_requests:
                self.requests[key] += 1
                return True
            return False
    