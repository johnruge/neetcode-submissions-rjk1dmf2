class TimeMap:

    def __init__(self):
        self.hashMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append((value, timestamp))
        else:
            self.hashMap[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap: return ""
        listVals = self.hashMap[key]
        lenList = len(listVals)
        l, r = 0, lenList

        if timestamp > listVals[-1][1]: return listVals[-1][0]
        if timestamp < listVals[0][1]: return ""

        while l < r:
            mid = (l + r) // 2

            val, tStamp = listVals[mid]
            if tStamp == timestamp:
                return val
            elif tStamp > timestamp:
                if mid - 1 >= 0 and listVals[mid - 1][1] <= timestamp:
                    return listVals[mid - 1][0]
                else:
                    r = mid - 1
            elif tStamp < timestamp:
                if mid + 1 < lenList and listVals[mid + 1][1] > timestamp:
                    return val
                else:
                    l = mid + 1

# set 0(1)
# get O(log n)
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)