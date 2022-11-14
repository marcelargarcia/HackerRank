# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# abcdefg
# abcdafgh

def lengthOfLongestSubstring(s):
    longest = 0
    s_built = ''
    for l in range(len(s)):
        letter = s[l]
        pos = s_built.find(letter)
        if pos != -1:
            s_built = s_built[pos+1:] + letter
        else:
            s_built = s_built + letter
        if len(s_built) > longest:
            longest = len(s_built)
    return longest


print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbbbbb'))
print(lengthOfLongestSubstring(''))
print(lengthOfLongestSubstring('abcdefgh'))
print(lengthOfLongestSubstring('abcdeabcdefghij'))