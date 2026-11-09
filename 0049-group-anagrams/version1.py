
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for i in strs: 
            count=[0]*26

            for c in i:
                count[ord(c)-ord('a')]+=1

            hashmap[tuple(count)].append(i) #If anagram exisits, append to exisiting letter count

        return list(hashmap.values())


#Time complexity : O(n.d),  Traversal thorugh every string in the array 'strs', and d being the number of characters in each of the string. 

#Space complexity : O(n), usage of dictionary. 
