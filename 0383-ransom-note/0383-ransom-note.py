class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency = Counter(magazine)
        
        for i in range(len(ransomNote)):
            if ransomNote[i] in frequency :
                if frequency[ransomNote[i]] > 0:
                    frequency[ransomNote[i]] -= 1
                else:
                    return False
            else:
                return False

        return True
