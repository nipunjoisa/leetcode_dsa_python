class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hashmap = defaultdict(int)
        ans = False
        if len(nums) > 1 :
            for idx in range(len(nums)) :
                if nums[idx] in hashmap : #duplicate
                    i = hashmap[nums[idx]]
                    j = idx
                    if abs(i-j) <= k:
                        return True
                    else:
                        ans = False
                hashmap[nums[idx]] = idx

        return ans

#Time complexity : O(n), due to operation per element in array when size of array is equal to n

#Space complexity : O(n), due to the storage of input elements in hashmap


            
    
