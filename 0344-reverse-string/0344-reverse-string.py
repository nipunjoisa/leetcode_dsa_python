class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1=0
        p2=len(s)-1
        while p1<=p2 :
            s[p1],s[p2] = s[p2],s[p1]
            p1+=1
            p2-=1

#Time complexity : O(n), where n is the number of characters in the list

#Space complexity: O(1), in place modification. 
        

