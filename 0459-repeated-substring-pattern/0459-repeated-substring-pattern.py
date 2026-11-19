class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
#Time complexity : O(n), building s+s string takes O(n) time and slicing it takes O(n) time, searching with in takes O(n) time
#Space complexity: O(n), creating the doubled string requires O(n) extra memory 