HASH_NUM = 2^31 - 1
class MyHashSet:
    def __init__(self):
        self.arr = [[] for n in range(HASH_NUM)]

    def add(self, key: int) -> None:
        arr = self.arr[key % HASH_NUM]
        for v in arr:
            if v == key:
                return
        arr.append(key)

    def remove(self, key: int) -> None:
        arr = self.arr[key % HASH_NUM]
        for i in range(len(arr)):
            if arr[i] == key:
                del arr[i]
                break
            
    def contains(self, key: int) -> bool:
        arr = self.arr[key % HASH_NUM]
        for v in arr:
            if v == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)