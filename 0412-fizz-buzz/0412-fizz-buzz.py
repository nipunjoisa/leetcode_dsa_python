class Solution:
    

    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        
        
        for i in range(1,n+1):
            
            if (i % 15 == 0) :
                result.append("FizzBuzz")
            elif (i % 3 == 0) :
                result.append("Fizz")
            elif ( i % 5 == 0) :
                result.append("Buzz")
            else:
                result.append(str(i))

        return result

    #Time complexity = O(n), one pass with constant work per number

    #Space complexity = O(n), due to the creation of list we return in the output. Extra space beyond ouput is O(1)
    

            
