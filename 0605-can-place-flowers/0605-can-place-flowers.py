class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                prev_empty = (i == 0 or flowerbed[i-1] == 0)
                print (f"{i} is {prev_empty} for prev_empty and {i == 0} and {flowerbed[i-1] == 0}")
                next_empty = (i == length - 1or flowerbed[i+1] == 0)
                print (f"{i} is {prev_empty} for next_empty and {i == 0} and {flowerbed[i-1] == 0}\n")
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    planted += 1
                
        return planted >= n