from collections import defaultdict,Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        counter = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]
        print(buckets)
        for num,freq in counter.items() :
            
            buckets[freq].append(num)
        ans = []
        for i in range(len(buckets)-1,0,-1) :
            if buckets[i] != 0:
                ans.extend(buckets[i])
            if len(ans) == k:
                return ans


        