class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency = Counter(magazine)
        
        for ch in ransomNote:
            if frequency[ch] == 0:        
                return False
            frequency[ch] -= 1
        return True


#Time complexity : O(m+r), where m is the len of magazine and r is the len ransomNote
#Space complexity : O(1), counter holds at most 26 keys, and it does not depend on input size. 
