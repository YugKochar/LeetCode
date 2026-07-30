class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = len(set(nums))
        y = len(nums)
        if x==y:
            return False
        else:
            return True
        