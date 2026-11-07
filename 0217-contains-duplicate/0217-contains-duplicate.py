class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False


#Time complexity: O(n), optimal when duplicate found early

#Space complexity O(n), due to the use of a set. 
        


        
            

        

        