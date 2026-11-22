class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l:int,r:int) -> [int,int]:
            while l>=0 and r<len(s) :
                if s[l] == s[r] :
                    l -= 1
                    r += 1
                else:
                    break
                
            return (l,r)

        L = 0
        R = 0
        for i in range(len(s)) :
            l_odd , r_odd = expand(i,i)
            if (r_odd - l_odd) > (R-L) :
                R=r_odd
                L=l_odd


            l_even , r_even = expand(i,i+1)
            if (r_even - l_even) > (R-L) :
                R=r_even
                L=l_even

        return s[L+1:R]

#Overall time : O(n^2)
#Overall Space: O(n)