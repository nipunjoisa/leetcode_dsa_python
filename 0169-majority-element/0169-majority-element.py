class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i]=1
        
        return max(hashmap,key=hashmap.get)

#Time complexity O(n)
#Space complexity O(n), due to the usage of dictionary