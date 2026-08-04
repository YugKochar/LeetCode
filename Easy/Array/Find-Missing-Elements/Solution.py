class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        missing = []
        for i in range(small+1, large):
            if i not in nums:
                missing.append(i)
        return missing
