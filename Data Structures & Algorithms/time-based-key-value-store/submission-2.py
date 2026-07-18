class TimeMap:

    def __init__(self):
        self.timeMap = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        entries = self.timeMap[key]

        l,r = 0, len(entries) - 1
        result = ""
        while l <= r:

            mid = (l + r) // 2
            value,time = entries[mid]

            if time <= timestamp:
                result = value
                l = mid + 1
            elif time > timestamp:
                r = mid - 1
        return result






        
