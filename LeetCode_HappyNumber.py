# https://leetcode.com/problems/happy-number

class Solution(object):
    def isHappy(self, n):
        output = n
        seen = set()

        while output != 1 and output not in seen:
            seen.add(output)
            n_list = list(str(output))
            output = 0
            for i in range(len(n_list)):
                output = output + (int(n_list[i]) ** 2)

        if output == 1:
            return True
        else:
            return False