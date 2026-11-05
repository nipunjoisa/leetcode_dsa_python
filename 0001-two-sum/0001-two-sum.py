class Solution:
    def twoSum(self,nums,target):
        n=len(nums)
        seen={}
        for i in range(0,n):
            current=nums[i]
            needed= target - current

            if needed in seen:
                return [seen[needed],i]
            else:
                seen[current]=i