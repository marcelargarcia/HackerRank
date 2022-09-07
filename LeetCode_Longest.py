# https://leetcode.com/problems/longest-substring-without-repeating-characters/
import sys

#O(N)
def lengthOfLongestSubstring(s):
    answ_set = set()
    max_answ = 0
    count = 0
    i = 0
    start = 0

    while i < len(s):
        if s[i] in answ_set:
            count = 0
            answ_set.clear()
            i = start + 1
            start = i
        answ_set.add(s[i])
        count += 1
        if max_answ < count:
            max_answ = count
        i += 1
    return max_answ


#O(N2)
def lengthOfLongestSubstring_2(s):
    s_dict = {}
    answ_set = set()
    max_answ = 0
    count = 0
    i = 0

    for k in range(len(s)):
        if s_dict.get(s[k], 'Not Found') == 'Not Found':
            s_dict[s[k]] = k
        else:
            value = s_dict.get(s[k])
            if not isinstance(s_dict[s[k]], list):
                s_dict[s[k]] = [value, k]
            else:
                s_dict[s[k]].append(k)
    while i < len(s):
        if s[i] in answ_set:
            count = 0
            answ_set.clear()
            i_list = s_dict.get(s[i])
            for j in range(len(i_list)):
                if i_list[j] == i:
                    break;
            i = i_list[j-1]+1
        answ_set.add(s[i])
        count += 1
        if max_answ < count:
            max_answ = count
        i += 1
    return max_answ

if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))
    print(lengthOfLongestSubstring('bbbbbb'))
    print(lengthOfLongestSubstring('pwwkew'))
    print(lengthOfLongestSubstring(''))
    print(lengthOfLongestSubstring(' '))
    print(lengthOfLongestSubstring('p'))
    print(lengthOfLongestSubstring('sdavdfabc'))


    print(lengthOfLongestSubstring_2('abcabcbb'))
    print(lengthOfLongestSubstring_2('bbbbbb'))
    print(lengthOfLongestSubstring_2('pwwkew'))
    print(lengthOfLongestSubstring_2(''))
    print(lengthOfLongestSubstring_2(' '))
    print(lengthOfLongestSubstring_2('p'))
    print(lengthOfLongestSubstring_2('sdavdfabc'))