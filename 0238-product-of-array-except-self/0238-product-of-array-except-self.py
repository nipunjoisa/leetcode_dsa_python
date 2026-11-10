class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix_product,suffix_product = [0]*n,[0]*n
        ans = []
        prefix_product[0]=1
        suffix_product[n-1] = 1
        
        for i in range(1,n):
            
            prefix_product[i] = prefix_product[i-1] * nums[i-1]

        for i in range(n-2,-1,-1) :
            
            suffix_product[i] = suffix_product[i+1] * nums[i+1]

        for i in range(0,n) :
            ans.append(prefix_product[i] * suffix_product[i] )

        return ans

#Time complexity overall : O(n-1) + O(n-1) + O(n) =O(n)

#Space complexity : O(3n) = O(n)

        
