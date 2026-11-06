class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)


        inverse = string[::-1]

        return (string==inverse)

    


#Space complexity, O(d), with d being the number of digits in int x

#Time complexity, at best case