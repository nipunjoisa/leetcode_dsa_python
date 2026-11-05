class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        
        COUNT = 0

        for i in nums:
            length=len(str(i))

            if length % 2 == 0:
                COUNT+=1
        return COUNT
        



