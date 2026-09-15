class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                count +=1
            else:
                count =0
            maxi = max(maxi, count)
        return maxi