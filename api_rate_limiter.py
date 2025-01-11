import time

class RateLimiter:
    def __init__(self, rate_limit=5, period=60):
        self.rate_limit = rate_limit
        self.period = period
        self.requests = {}

    def allow_request(self, user_id):
        current_time = time.time()

        # Clean up old requests that are outside the period window
        if user_id in self.requests:
            self.requests[user_id] = [timestamp for timestamp in self.requests[user_id] if current_time - timestamp < self.period]

        # Allow request if under rate limit
        if len(self.requests.get(user_id, [])) < self.rate_limit:
            if user_id not in self.requests:
                self.requests[user_id] = []
            self.requests[user_id].append(current_time)
            return True
        
        return False

# Example usage
rate_limiter = RateLimiter(rate_limit=3, period=10)
user_id = "user123"

# Test if a request is allowed
if rate_limiter.allow_request(user_id):
    print("Request allowed")
else:
    print("Rate limit exceeded")
