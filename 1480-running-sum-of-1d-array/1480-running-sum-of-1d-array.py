class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        
        
        length = len(nums)
        result = [0]*length
        result[0]=nums[0]
        for i in range(1,length):
            result[i]=nums[i]+result[i-1] 
        return result


    
        