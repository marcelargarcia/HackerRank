#https://leetcode.com/problems/evaluate-reverse-polish-notation
def evalRPN(tokens):
    stack = []
    output = 0
    ops = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y),
           '*': (lambda x, y: x * y), '/': (lambda x, y: int(x / y))}
    if len(tokens) < 3:
        return tokens[0]
    for i in range(len(tokens)):
        char = tokens[i]
        if ops.get(char,'None') == 'None': #Number
            stack.append(char)
        else: #Operator
            int2 = int(stack.pop())
            int1 = int(stack.pop())
            output = int(ops[char](int1, int2))
            stack.append(output)
    return output

print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(evalRPN(["4","-2","/","2","-3","-","-"]))

# RPN = reverse polish notation
# Input: list with chars
# Output: sum of the expression
# Strategy:
# Create one stack: with numbers
    # When an operator appears, we will pop two elements of the stack,
    # if the stack doesnt have 2 elements, we will pop the last
    # and get the output

#Edge cases:
# [14,'+'] = 14
# [18] = 18
# ['+'] = ?
