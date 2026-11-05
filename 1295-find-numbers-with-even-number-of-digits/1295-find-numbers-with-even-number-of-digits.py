
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        
        count = 0

        for i in nums:
            digits = 0
            while i>0:
                i //=10
                digits+=1

            if digits % 2 == 0:
                count+=1

        return count

            

        #Time complexity of O(n) 

        #Space complexity of O(d). 



