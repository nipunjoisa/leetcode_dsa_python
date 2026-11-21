class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        res = ''
        def expand(l:int,r:int) -> str :
            while l >= 0 and r < n :          #Time: O(n)
                if s[l] == s[r] :
                    l -= 1
                    r += 1
                else:
                    break

            return s[l+1:r]


        for i in range(n) :           #Time O(n^2)
            odd = expand(i,i)
            if len(odd) > len(res):
                res = odd

            even = expand(i,i+1)
            if len(even) > len(res) :
                res = even

        return res

#Overall time :O(n)
#Overall space: O(1), res is string variables, n integer variable
