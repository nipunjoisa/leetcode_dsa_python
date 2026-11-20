class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0
        for c in s:     #Time : O(n), O(1) operation for every character 
            count[c] += 1

            if count[c]%2 == 0:  #Every even pair forms a palindrome, add 2 everytime you notice it
                res += 2

        for i in count.values() : #O(n)
            if i%2 != 0: 
                res+=1
                break

        return res
#Time : O(n)
#Space: O(n)