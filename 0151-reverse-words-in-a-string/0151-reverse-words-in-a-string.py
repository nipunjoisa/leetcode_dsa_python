class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        return(' '.join(a[::-1]))
#Time complexity : O(n)
#Space complexity : O(n)
