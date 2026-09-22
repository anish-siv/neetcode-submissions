class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        lo = 0
        hi = len(values) - 1
        result = ""
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                result = values[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return result