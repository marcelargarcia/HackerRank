#https://www.hackerrank.com/challenges/balanced-brackets/problem
import sys

def isBalanced(string):
    stack = []
    if len(string) % 2 != 0:
        return 'NO'

    for i in range(len(string)):
        if string[i] != ')' and string[i] != ']' and string[i] != '}':
            stack.append(string[i])
        else:
            if not stack:
                return 'NO'

            top = stack.pop()
            if (string[i] == ']' and top != '[') \
                    or (string[i] == ')' and top != '(') \
                    or (string[i] == '}' and top != '{'):
                return 'NO'
    if stack:
        return 'NO'

    return 'YES'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()


# ]]
# [](){()}
# [(}}
# []()
# [[

# [](){()}
# [
# [[[[[[[[[[]]]]]]]]]]]
