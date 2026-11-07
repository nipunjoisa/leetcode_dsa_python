class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        
        profit = 0

        for price in prices[1:] :

            if price < lowest :
                lowest = price
            else:
                profit = max(profit,price-lowest)

        return profit

        

#Time complexity : O(n), traversing through the array n-1 times, every pass

#Space complexity : O(1), using three variables. 