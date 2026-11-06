class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)

        point1=0
        point2=len(string)-1

        while point1<=point2:
            if string[point1]!=string[point2] :
                return False

            point1+=1
            point2-=1

        return True