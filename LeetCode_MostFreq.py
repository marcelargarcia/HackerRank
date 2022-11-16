#https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter

def topKFrequent(nums, k):
    hashFreq = {}
    hashFreq2 = {}
    resp = []

    hashFreq = Counter(nums)

    for num, freq in hashFreq.items():
        key = freq
        value = hashFreq2.get(key,'')
        if value == '':
            hashFreq2[key] = [num]
        else:
            hashFreq2[key].append(num)

    for key in sorted(hashFreq2.keys(), reverse=True):
        if len(resp) == k:
            break
        v = hashFreq2.get(key)
        if len(v) >= (k-len(resp)):
            resp.extend(v[:k])
        if len(v) < (k-len(resp)):
            resp.extend(v)

    return resp

print(topKFrequent([1,1,1,2,2,3],2))

