import time

class RateLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.requests = {}

    def allow_request(self, user):
        current_time = time.time()

        if user not in self.requests:
            self.requests[user] = []

        self.requests[user] = [
            t for t in self.requests[user] if current_time - t < self.window
        ]

        if len(self.requests[user]) < self.limit:
            self.requests[user].append(current_time)
            return True
        return False

limiter = RateLimiter(3, 10)

user = "user1"
for i in range(5):
    print("Request", i + 1, "Allowed:", limiter.allow_request(user))
    time.sleep(2)
