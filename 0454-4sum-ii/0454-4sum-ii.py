class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:

        n = len(nums1)
        hashmap = defaultdict(int)

        for i in range(n):
            for j in range(n):
                current = nums1[i] + nums2[j]
                hashmap[current] += 1
        count = 0
        for i in range(n):
            for j in range(n) :
                target = -(nums3[i]+nums4[j])
                if target in hashmap :
                    count+= hashmap[target]

        return count

#Time complexity : O(n^2)
#Space complexity: O(n^2), if all pair sums are different.  