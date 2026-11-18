class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        total = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i+1]] > roman[s[i]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total 

#Time complexity : O(n), every element in the string is worked upon once per iteration. 
#Space complexity: O(n), due to the use of dictionary 