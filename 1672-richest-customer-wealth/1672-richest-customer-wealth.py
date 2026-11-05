class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest=0 

        for i in accounts:
            wealth=0

            for j in i:
                wealth+=j


            richest=max(richest,wealth)


        return richest