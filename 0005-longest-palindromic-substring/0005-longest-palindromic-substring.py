class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        
        def expand(l:int,r:int) -> str:
            while l >= 0 and r < n :
                if s[l] == s[r] :
                    l -= 1
                    r += 1

                else:
                    break

            return s[l+1:r]

        for i in range(n):

            #ODD

            odd = expand(i,i)
            if len(odd) > len(res) :
                res = odd
                

            
            even = expand(i,i+1)
            if len(even) > len(res) :
                res = even
                

        return res

        
            

        