import math
class Solution:
    def compute(self,piles, hourly):
            totalhrs = 0
            for bananas in piles:
                totalhrs += math.ceil(bananas/hourly)
            return totalhrs
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpiles = max(piles)
        ans = maxpiles
        low = 1
        high = max(piles)
        while low <=high:
            mid = (low+high)//2
            totalhrs = self.compute(piles, mid)
            if totalhrs <=h:
                ans = mid
                high = mid-1
            else:
                low = mid +1
        return ans

        
    