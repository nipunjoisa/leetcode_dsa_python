class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        
        COUNT = 0

        for i in nums:
            length=len(str(i))

            if length % 2 == 0:
                COUNT+=1
        return COUNT

        #Time complexity of O(n.d) on a single pass, to traverse through every element in nums, and d is the number of digits when we are counting the strings. 

        #Space complexity of O(1). 


