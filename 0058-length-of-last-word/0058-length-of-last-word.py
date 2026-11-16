class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        while i>=0 and s[i] == " ": #if there are whitespace at the end of the string,skip them before we start counting. 
            i-=1
        
        while i>=0 and s[i]!=" ":
            length += 1
            i-=1
        
        return length

#Time complexity :O(n)
#Space complexity : O(1)

        
            

        





