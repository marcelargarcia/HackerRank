import random

class RandomizedSet(object):
    def __init__(self):
        self.rSet = set()

    def insert(self, val):
        if val not in self.rSet:
            self.rSet.add(val)
            return True
        else:
            return False



    def remove(self, val):
        if val not in self.rSet:
            return False
        else:
            self.rSet.remove(val)
            return True

    def getRandom(self):
        ran = random.choices(list(self.rSet), k=1)
        return int(ran[0])

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(2))
print(obj.insert(3))
print(obj.insert(8))
print(obj.insert(10))
print(obj.insert(10))

print(obj.remove(10))
print(obj.remove(1))

print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())