class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
       
        pairs = 0
        hashmap = Counter(nums)
        print(hashmap)
        for n,i in hashmap.items():
            pairs += (i*(i-1))//2
        return pairs

#Time complexity :  O(n)
#Space complexity : O(n)


