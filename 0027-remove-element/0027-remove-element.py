class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write = 0

        for i in range(len(nums)) :
            if nums[i] != val :
                nums[write] = nums[i]
                write += 1
        return write 

#Time complexity : O(n), traversing the size of array.

#Space complexity : O(1), constant space editing of array

                