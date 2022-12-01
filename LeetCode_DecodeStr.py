#https://leetcode.com/problems/decode-string/discussion/

class Solution(object):
    def decodeString(self, s):
        output = ''
        dig = ''
        stack = []
        for c in range(len(s)):
            if s[c].isdigit():
                dig = dig + s[c]
                if c < len(s) - 1 and not s[c+1].isdigit():
                    stack.append((output, dig))
                    dig = ''
            elif s[c].isalpha():
                output = output + s[c]
            elif s[c] == ']':
                lastoutput, num = stack.pop()
                dif = output[len(lastoutput):]
                output = str(lastoutput) + str(dif) * int(num)
        return output
so = Solution()
# print(so.decodeString("3[a2[c]a]"))
# print(so.decodeString("2[abc]3[cd]ef"))
print(so.decodeString("3[a]2[bc]"))
# print(so.decodeString("3[a2[c]]"))
# print(so.decodeString("3[aa]"))
print(so.decodeString("100[leetcode]"))