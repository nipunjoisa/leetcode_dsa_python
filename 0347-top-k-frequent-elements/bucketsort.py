from collections import defaultdict,Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        counter = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]
        
        for num,freq in counter.items() :
            
            buckets[freq].append(num)
        ans = []
        for i in range(len(buckets)-1,0,-1) :
            if buckets[i]:
                ans.extend(buckets[i])
            if len(ans) == k:
                return ans


#Time complexity : O(n). [ O(n) to initialise buckers, O(n)to append to buckets, and O(n), to reverse traverse buckets to fetch the most freqent k elements].

#Space complexity: O(n). due to usage of arrays of ans and buckets. 



        
