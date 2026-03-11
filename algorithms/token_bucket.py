import time
from threading import Lock

class TokenBucketLimiter:

    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.buckets = {}
        self.lock = Lock()

    def allow_request(self, client_id):

        with self.lock:

            if client_id not in self.buckets:
                self.buckets[client_id] = {
                    "tokens": self.capacity,
                    "last_refill": time.time()
                }

            bucket = self.buckets[client_id]

            now = time.time()
            elapsed = now - bucket["last_refill"]

            refill = elapsed * self.refill_rate
            bucket["tokens"] = min(self.capacity, bucket["tokens"] + refill)
            bucket["last_refill"] = now

            if bucket["tokens"] >= 1:
                bucket["tokens"] -= 1
                return True

            return False