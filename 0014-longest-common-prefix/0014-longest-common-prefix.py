class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        m = min(len(i) for i in strs) #O(n)
    
        for i in range(m) :
            char = strs[0][i]
            for word in strs:
                if word[i] != char :
                    return strs[0][:i]
            
        return strs[0][:m]

#Time complexity : O(n.m), iteration through every string, and the character a minimum of m times, where m is the length of the shortest word in input array

#Space Complexity : O(1). 