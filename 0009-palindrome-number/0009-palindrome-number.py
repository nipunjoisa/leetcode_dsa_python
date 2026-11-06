class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''string = str(x)


        inverse = string[::-1]

        return (string==inverse)'''

        temp = x
        reverse = 0
        if x < 0:
            return False

        while temp != 0:
            last_digit = temp % 10
            reverse = reverse*10 + last_digit
            temp = temp//10

        return(reverse==x)
            


#Space complexity, O(d), with d being the number of digits in int x

#Time complexity, at best case