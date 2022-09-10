# https://www.hackerrank.com/challenges/stockmax/problem
# O(N)

import sys

#[1,2,100,2,3,98]
def stockmax(prices):
    maxPrice = prices[len(prices)-1]
    profit = 0
    for i in reversed(range(0,len(prices)-1)):
        if maxPrice > prices[i]:
            profit = profit + (maxPrice - prices[i])
        elif prices[i] > maxPrice:
            maxPrice = prices[i]
    return profit



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()