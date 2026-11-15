class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        swap = 1 
        for i in range(1,len(nums)) :
            if nums[i-1] != nums[i] :
                nums[swap]=nums[i]
                swap += 1
        return swap


#Time complexity : O(n)
#Space complexity : O(1)

        
