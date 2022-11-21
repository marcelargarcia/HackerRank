#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    if not prices:
        return 0
    bestPrice = [0]*len(prices)
    for i in reversed(range(len(prices))):
        if i == len(prices)-1:
            bestPrice[i] = prices[i]
        else:
            if prices[i] > bestPrice[i+1]:
                bestPrice[i] = prices[i]
            else:
                bestPrice[i] = bestPrice[i+1]

    maxProfit = 0
    for j in range(len(prices)):
        diff = bestPrice[j] - prices[j]
        if diff > maxProfit:
            maxProfit = diff

    return maxProfit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

#Input: array with prices
#Output: max profit
#Strategy:
    # Reversed loop
    # Create a list with best price in the moment
#Complexity
    # Time complexity O(N)
    # Space complexity O(N)
#Trade offs?
# Edge Cases
    #[7,6,5,4,3] = 0
    #[1] = 0
    #[] = 0
    #[0] = 0
    #[1,5] = 4