#https://leetcode.com/problems/jewels-and-stones

from collections import Counter

#Solution 1
def numJewelsInStones(jewels, stones):
    hashFreq = Counter(stones)
    num = 0
    for k, v in hashFreq.items():
        if jewels.find(k) != -1:
            num += v
    return num



# Solution 2
def numJewelsInStones_2(jewels, stones):
    jewelsSet = createSetJewels(jewels)
    num = 0
    for s in range(len(stones)):
        key = stones[s]
        if key in jewelsSet:
            num +=1
    return num

def createSetJewels(jewels):
    jewelsSet = set()
    for i in range(len(jewels)):
        key = jewels[i]
        jewelsSet.add(key)

    return jewelsSet

print(numJewelsInStones('aA','aAAbbbb'))
print(numJewelsInStones('z','ZZ'))