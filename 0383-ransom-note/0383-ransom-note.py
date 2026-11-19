class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False

        return True
# Time:  O(k*(m+r))  k = distinct letters in the note (<= 26, so O(m+r) here)
# Space: O(1)        set of at most 26 letters
