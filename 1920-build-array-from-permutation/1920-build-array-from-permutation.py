class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        length = len(nums)
        ans = [0]*length

        for i in range(length):
            ans[i] = nums[nums[i]]

        return ans
#Time complexity : O(n) extra space due to array ans. 