class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for i in nums:
            seen.add(i)

        return not(len(seen) == len(nums))
        


        
            

        

        