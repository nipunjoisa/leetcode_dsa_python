class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums) 
        num1=set(nums)
        
        ans = []
        for i in range(1,n+1) :
            if i not in num1:
                ans.append(i)

        return ans

#Time complexity : O(n)
#Space complexity: O(n), storage in set. 