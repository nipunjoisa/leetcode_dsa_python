class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num!=0:
            if num % 2 == 0:
                num //= 2
            else:
                num -=1

            step+=1

        return step

#Time complexity: At most, at every two steps,the num is halved, therefore time complexity would be 2.O(log n) = O(log n )

#Space complexity of O(1), one integer counter 'step' 