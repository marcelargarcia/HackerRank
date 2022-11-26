#https://leetcode.com/problems/lru-cache/
#Fazer de novo com heap

from collections import deque

class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.LRUqueue = deque()
        self.LRUCache = {}

    def get(self, key):
        if key in self.LRUqueue:
            self.LRUqueue.remove(key)
            self.LRUqueue.append(key)
        return self.LRUCache.get(key,-1)

    def put(self, key, value):
        if key in self.LRUqueue:
            self.LRUqueue.remove(key)
        elif len(self.LRUqueue) == self.capacity:
            leastUsed = self.LRUqueue.popleft()
            self.LRUCache.pop(leastUsed)
        self.LRUqueue.append(key)
        self.LRUCache[key] = value

        return None


obj = LRUCache(2)
print(obj.get(2))
print(obj.put(2,6))
print(obj.get(1))
print(obj.put(1,5))
print(obj.put(1,2))
print(obj.get(1))
print(obj.get(2))


#
# print(obj.put(1,1))
# print(obj.put(2,2))
# print(obj.get(1))
# print(obj.put(3,3))
# print(obj.get(2))
#
