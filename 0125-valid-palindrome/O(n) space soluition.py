class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ''
        for ch in s:
            if ch.isalnum():
                stripped += ch

        p1=0
        p2=len(stripped) - 1

        while p1<=p2:
            if stripped[p1].lower() != stripped[p2].lower() :
                return False
            p1 += 1
            p2 -= 1

        return True 

#Time complexity :O(n), Stripping took O(n) time, and comparision took n//2 time, therefore overall O(n)

#Space complexity: O(n), the string stripped in worst case could store all the strings if all .isalnum() is true. 

       
        
                
