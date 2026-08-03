class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = 1<<n
        ans = []
        for num in range(subset):
            subset = []
            for i in range(n):
                if num & (1<<i):
                    subset.append(nums[i])
            ans.append(subset)
        return ans
