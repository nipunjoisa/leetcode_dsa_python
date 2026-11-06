class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        write = 0

        if len(nums)>1:
            for i in range(len(nums)):
                if nums[i] != 0 :
                    temp = nums[write]
                    nums[write] = nums[i]
                    nums[i] = temp
                    write += 1
        

            
#Time complexity O(n), traversing array of size 'n'
#Space complexity O(1), using constant space for modification







#swap 0 with the NEXT non-zero element

        '''write = 0

        for i in range(len(nums)) :
            if nums[i] == 0 :
                write+=1
            else:
                nums[write]=nums[i]'''

        
        