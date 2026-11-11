class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapped = {}

        for i in range(len(s)) :
            if s[i] in mapped :
                if mapped[s[i]] != t[i]:
                    return False            
            else :
                if t[i] in mapped.values():
                    return False
                mapped[s[i]] = t[i]
        return True

#Time comoplexity: O(n), for every input size, the code runs for n times.

#Space complexity : O(n), due to the use of hashmap dictionary 


