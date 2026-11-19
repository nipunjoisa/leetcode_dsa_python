class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not(Counter(ransomNote) - Counter(magazine))


#Time complexity : O(m+r), counter(ransomnote) takes O(m) times, where m is the number of characters in magazine and similarly O(r) for ransomnote

#Space complexity : O(1), constant hashmap which can store at most 26 lowercase characters for any input. 
