import collections

class Cache:
    # Using deque as a cache by appending we mimic LFU behavior. I wasn't sure how to implement this at first so I referenced the example solution.
    # Inside the cache we have a list of tuples. The first element of the tuple is the address and the second element is the value.
    def __init__(self):
        self.size = 16
        self.cache = collections.deque(maxlen=self.size)
        self.flush()

    # Repeatedly append an empty tuple to the cache to flush it.
    def flush(self):
        for i in range(self.size):
            self.cache.append(("", ""))

    def read(self, address):
        for i in range(len(self.cache)):
            if self.cache[i][0] == address:
                return self.cache[i][1]
        return None

    def write(self, address, value):
        self.cache.append(tuple((address, value)))