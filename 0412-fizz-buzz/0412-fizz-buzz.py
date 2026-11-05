class Solution:
    

    def fizzBuzz(self, n: int) -> list[str]:
        result = [""]*n
        
        
        for num in range(n):
            i = num+1
            if (i % 5 == 0) and ( i % 3 == 0) :
                result[num]="FizzBuzz"
            elif (i % 3 == 0) :
                result[num]="Fizz"
            elif ( i % 5 == 0) :
                result[num]="Buzz"
            else:
                result[num]=str(i)

        return result

            
