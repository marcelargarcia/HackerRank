class Solution(object):
    def decodeString(self, s):
        output = ''
        stack = []
        for c in range(len(s)):
            if s[c].isdigit():
                stack.append((output, s[c]))
            elif s[c].isalpha():
                output = output + s[c]
            elif s[c] == ']':
                lastoutput, num = stack.pop()
                dif = output[len(lastoutput):]
                if dif == '' or lastoutput == '':
                    output = str(lastoutput) * int(num)
                else:
                    output = str(lastoutput) + str(dif) * int(num)
                #output = ''
        return output
so = Solution()
print(so.decodeString("3[a2[c]a]"))
