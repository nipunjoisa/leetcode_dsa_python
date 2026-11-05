class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest=0 

        for customer in accounts:
            wealth=0

            for amount in customer:
                wealth+=amount


            richest=max(richest,wealth)


        return richest