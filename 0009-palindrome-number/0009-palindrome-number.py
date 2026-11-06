class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)


        inverse = string[::-1]

        return (string==inverse)