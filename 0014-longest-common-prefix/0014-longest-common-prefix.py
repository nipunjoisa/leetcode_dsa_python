class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        n = min(len(i) for i in strs) #O(n)
    
        for i in range(n) :
            char = strs[0][i]
            for word in strs:
                if word[i] != char :
                    return strs[0][:i]
            
        return strs[0][:n]