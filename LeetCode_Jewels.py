
def numJewelsInStones(jewels, stones):
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