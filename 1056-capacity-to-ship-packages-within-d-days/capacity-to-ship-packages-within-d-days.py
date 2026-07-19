class Solution:
    def daysNeeded(self, weights, capacity):
        days = 1
        load = 0
        for w in weights:
            if load+w > capacity:
                days += 1
                load = w
            else:
                load +=w
        return days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low<high:
            mid = (low+high) //2
            x = self.daysNeeded(weights,mid)
            if x <=days:
                high = mid 
            else:
                low = mid +1
        return low
        