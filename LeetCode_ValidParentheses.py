#https://leetcode.com/problems/valid-parentheses

def isValid(s):
    opened = ['(', '[', '{']
    opened_stack = []

    if len(s)%2 !=0:
        return False
    s = list(s)
    for i in range(len(s)):
        if s[i] in opened:
            opened_stack.append(s[i])
        else:
            cl = s[i]
            if opened_stack:
                op = opened_stack.pop()
                if (op == '(' and cl != ')') or (op == '[' and cl != ']') or (op == '{' and cl != '}'):
                    return False
            else:
                return False
    if opened_stack:
        return False
    return True

print(isValid("){"))
print(isValid("(("))
print(isValid("([)]"))
print(isValid("([])"))
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("((((()))))"))
print(isValid("(]"))
#Edge Cases: "[]", "(((())))","([)]", "]]", "[[", 