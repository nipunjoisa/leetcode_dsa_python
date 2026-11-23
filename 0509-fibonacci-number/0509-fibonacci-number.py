class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)


#Time complexity :O(2^n), every tree level increases by roughly 2^n nodes with each node doing O(1) work. 

#Space complexity : O(n), branch wise execution from python, with each recursive call pausing current branch and exploring all the way down(usually left first, frames popped and then the right side is explored )

