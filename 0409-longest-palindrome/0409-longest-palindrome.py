class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0
        for ch in s:
            count[ch] += 1

            if count[ch] % 2 == 0:
                res += 2
        
        for i in count.values():
            if i%2 != 0:
                return res + 1
        return res
