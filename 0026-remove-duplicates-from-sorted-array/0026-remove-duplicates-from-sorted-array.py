class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #sorted in ascending order. 
        
        write = 1
        
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1] : #unique element found
                nums[write] = nums[i] #swap it with the last noted unique position
                
                write += 1
        return write


#time complexity : O(n), n traversals through the array nums with size n
#space complexity : O(1), constant space modification. 



                

        

                
             
            