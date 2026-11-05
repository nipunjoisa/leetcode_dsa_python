class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        
        for i in range(len(nums)):
            nums[i]=str(nums[i])

        COUNT=0
        

        for i in nums:
            count = 0
            for j in i:
                count+=1
            if count%2==0:
                COUNT+=1
            
            
        return COUNT



