#https://leetcode.com/problems/group-anagrams
def groupAnagrams(strs):
    mapSortedWords = {}
    resultList = []
    for i in range(len(strs)): #O(N)
        word = strs[i]
        key = ''.join(sorted(word)) #O(logN) quick sort
        if mapSortedWords.get(key,'Not Found') == 'Not Found':
            mapSortedWords[key] = [word]
        else:
            value = mapSortedWords.get(key)
            mapSortedWords[key].append(word)

    for key, value in mapSortedWords.items():
        resultList.append(value)

    return resultList


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

#################################################################
#Input: 1 list of strings
#Output: 1 list with multiple lists of anagrams grouped

# 1 Strategy
    # Map each string to their ordered (sorted) string.
    # [ate, eat, tea] ->
    # ate -> ate
    # eat -> ate
    # tea -> ate
    #["eat","tea","tan","ate","nat","bat"]
    # "ate" -> eat, tea, ate

    #Time complexity: O(N logN) = O(N) + O(log N) (quick sort)
    #Space complexity: O(N) = create a new hash map

#Edge cases:
    # Has no value [""] -> [[""]]
    # Has 1 value ["eat"] -> [["eat"]]
    # >1 ["tan", "eat"] -> [["tan"], ["eat"]]




