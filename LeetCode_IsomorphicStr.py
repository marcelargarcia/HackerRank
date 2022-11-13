#https://leetcode.com/problems/isomorphic-strings

def isIsomorphic(s, t):
    mapLetter = {}
    if len(s) != len(t):
        return False
    newStr = s
    i = 0
    while i < len(s):
        letter = s[i]
        newLetter = t[i]
        if letter not in mapLetter.keys() and newLetter not in mapLetter.values():
            mapLetter[letter] = newLetter

        if letter in mapLetter.keys() and mapLetter[letter] == newLetter:
            newStr = newStr[:i] + newLetter + newStr[i+1:]
        else:
            newStr = newStr[:i] + '*' + newStr[i + 1:]
        i = i+1
    if newStr == t:
        return True
    return False

print(isIsomorphic('abab','baba'))
print(isIsomorphic('foo','bar'))
print(isIsomorphic('egg','add'))
print(isIsomorphic('badc','baba'))
print(isIsomorphic('paper','title'))
print(isIsomorphic('egcd','adfd'))