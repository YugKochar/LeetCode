class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        currMax = maxSum = nums[0]
        currMin = minSum = nums[0]
        n = len(nums)
        for i in range(1, n):
            currMax = max(nums[i], currMax + nums[i])
            maxSum = max(maxSum, currMax)
            currMin = min(nums[i], currMin + nums[i])
            minSum = min(minSum, currMin)
        if maxSum <0:
            return maxSum

        return max(maxSum, totalSum - minSum)

