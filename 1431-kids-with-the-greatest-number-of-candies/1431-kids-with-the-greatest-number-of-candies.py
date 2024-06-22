class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_candies = max(candies)
        candies_boolean = []
        for i in range(len(candies)):
            if candies[i] + extraCandies < greatest_candies:
                candies_boolean.append(False)
            else:
                candies_boolean.append(True)
        
        return candies_boolean
                
        
        