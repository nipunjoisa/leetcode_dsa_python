class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1,(n//2)+1):
            if n%i == 0:
                substring = s[:i]
                m = len(substring)
                if substring*(n//m) == s:
                    return True

        return False
#Time complexity : O(n .d(n)), where d(n) is the number of divisors of n. 
#Space complexity: O(n)
