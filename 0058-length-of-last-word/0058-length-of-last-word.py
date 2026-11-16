class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = s.split()                 
        return(len(k[-1]))


#Time complexity :O(n), the split function takes O(n) time
#Space complexity:O(n), extra space by the array 'k' 