import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def possible(d):
            total = 0
            for num in nums:
                total += math.ceil(num/d)
            return total<=threshold
        low = 1
        high = max(nums)
        while low <= high:
            mid =(high+low)//2
            if possible(mid):
                high = mid-1
            else:
                low = mid+1
        return low