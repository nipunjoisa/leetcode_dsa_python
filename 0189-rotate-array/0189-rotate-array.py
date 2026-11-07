class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*len(nums)

        for i in range(len(nums)) :
            res[(i+k)%len(nums)] = nums[i]

        for i in range(len(nums)) :
            nums[i] = res[i]

#Time complexity : O(n)
#Space complexity : O(n)

        

