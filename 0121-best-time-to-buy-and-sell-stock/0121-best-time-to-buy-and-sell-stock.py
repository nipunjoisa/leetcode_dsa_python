class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        highest = prices[0]
        profit = 0

        for i in range(1,len(prices)) :

            if prices[i] < lowest :
                lowest = prices[i]
                highest = 0
                continue
            if prices[i] > highest:
                highest = prices[i]

            profit = max(profit,(highest-lowest))


        return profit