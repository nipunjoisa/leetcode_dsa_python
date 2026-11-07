class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()

        return(nums[len(nums)//2]) 

        #Because majority element appears more than [n/2] times, so i would be from the middle of the list to the end, and easy to find. 

    #Time : O(1)
    #Space: O(1)