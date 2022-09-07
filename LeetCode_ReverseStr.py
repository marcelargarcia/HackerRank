#https://leetcode.com/problems/reverse-string/

#Time: O(N)
#Memory: O(1)
def reverseString(s):
    right = len(s) -1

    for left in range(0, int(round(len(s)/2))):
        first = s[left]
        second = s[right]
        s[right] = first
        s[left] = second

        right -= 1
    print(s)


#Time: O(N)
#Memory: O(N)
def reverseString_2(s):
    ans = []
    for i in reversed(range(len(s))):
        ans.append(s[i])
    s = str(ans)
    print(s)

if __name__ == '__main__':
    reverseString(["h","e","l","l","o"])
    reverseString(["H","a","n","n","a","h"])
