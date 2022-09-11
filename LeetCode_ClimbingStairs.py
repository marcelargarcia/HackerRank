# https://leetcode.com/problems/climbing-stairs/
import math

def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    return climbStairs(n-1)+climbStairs(n-2)

if __name__ == '__main__':
    print(climbStairs(2))
    print(climbStairs(3))
    print(climbStairs(4))
    print(climbStairs(5))
    print(climbStairs(6))


