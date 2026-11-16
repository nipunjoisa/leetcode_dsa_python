class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        n = min(len(i) for i in strs) #O(n)
    
        for i in range(n) :
            char = strs[0][i] #First word in list being used as reference. 
            for word in strs[1::] :
                if word[i] != char :
                    return strs[0][:i]

        return strs[0][:n]