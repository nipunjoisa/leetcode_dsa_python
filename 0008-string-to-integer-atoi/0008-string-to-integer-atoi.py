class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip() #removing leading whitespace using Lstrip() function , part of the python std library , takes O(n) time scanning left to right and removing white space. 

        #handling edge case where s="" 
        if not s:   
            return 0

       
        
        #use sign = 1 or -1 to keep track of negative or positive number. 

        sign = 1 #default is positive
        digit = 0 #result is stored here mathematically 

        if s[0] == '+' or s[0] =='-' :
            if s[0] == '-' :
                sign = -1
            s=s[1:] #slice the rest of the string, takens O(n) time
        
        for ch in s:            #Time here: O(n)
            if not ch.isdigit():
                break
            digit = digit * 10 + int(ch)       #constructing the digit left to right, O(1) operation

        digit = digit * sign
        #handling size limit 
        if digit < (-2**31):
            return -2**31
        elif digit > (2**31 - 1):
            return 2**31 - 1

        return digit

#ovr Time complexity : O(n)
#Space complexity : O(n), .strip() and slicing creates copies of strings and allocates space upto n, whereas the int varaibles takes O(1) space