# https://leetcode.com/problems/zigzag-conversion/

def convert(s, numRows):
    i = 0
    newS = ""
    if len(s) == 1 or numRows == 1:
        return s
    while i < numRows:
        j = i
        on = True
        while len(s) > j >= 0:
            if (on and i != 0 and i != numRows - 1) or i == 0:
                newS = newS + s[j]
                j = j + ((2 * numRows) - (2 * i) - 3) + 1
            elif (not on and i != 0 and i != numRows - 1) or i == numRows - 1:
                newS = newS + s[j]
                j = j + (2 * i)
            on = not on
        i = i + 1

    return newS


if __name__ == '__main__':
    print(convert('PAYPALISHIRING', 4))
    print(convert('PA', 2))
    print(convert('P', 1))
    print(convert('PA', 1))