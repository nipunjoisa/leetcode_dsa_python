from collections import defaultdict,Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        
        return(sorted(hashmap,key=hashmap.get,reverse=True)[:k])
#Time complexity :O(n log n), traversing list nums, n times, and sorting takes log n time

#Space complexity : O(n), extra space occupied by dictionary. 



        
