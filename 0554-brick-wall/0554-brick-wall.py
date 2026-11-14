class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n=len(wall)
        hashmap = defaultdict(int)
        
        for i in range(n):
            position = 0
            count = 0
            for j in range(len(wall[i])-1) :
                position += wall[i][j]
                hashmap[position] += 1

        return (len(wall) - max(hashmap.values(),default = 0))


# Time:  O(m), m = total number of bricks (each brick visited once)
# Space: O(m) worst case: one dict key per distinct edge position


        

        


            

        
        



