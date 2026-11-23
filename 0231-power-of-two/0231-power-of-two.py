class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: #any power of 2 is never zero
            return False
        if n==1: #2 to the power of 0 is always one
            return True 
        if n % 2 != 0:
            return False

        return self.isPowerOfTwo(n//2)

#Time Complexity : O(log n), input space is halved every traversal, with O(1) work.

#Space Complexity : O(log n), amximum stack depth is log n frames, due to log n recursive calls. 
        

        