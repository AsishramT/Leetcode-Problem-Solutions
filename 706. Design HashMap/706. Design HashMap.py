
class MyHashMap:

    def __init__(self):
        self.arr=[-1]*1000001

    def put(self, key: int, value: int) -> None:
        self.arr[key]=value
        

    def get(self, key: int) -> int:
        return self.arr[key]
        

    def remove(self, key: int) -> None:
        self.arr[key]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

#note: This implementation uses a fixed-size array to store the values, which is efficient for the given constraints (keys in the range [0, 10^6]). The `put`, `get`, and `remove` methods operate in O(1) time complexity.
#downside: This implementation uses a large amount of memory regardless of the number of keys actually stored, which may not be efficient for sparse data.
#O(1) time complexity for put, get, and remove operations. O(1) space complexity for the array, but it uses a fixed size of 1,000,001 elements.