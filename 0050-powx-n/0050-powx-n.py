class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n<0:
            return 1/self.myPow(x,-n)

        half = self.myPow(x,n//2)

        if n%2 != 0:
            return half*half*x
        else:
            return half*half

#Time complexity: O(log n), halved every call.
#Space complexity : O(log n), upto log n frames stored. 