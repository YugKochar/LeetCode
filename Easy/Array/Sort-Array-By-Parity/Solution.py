class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        evenArr = []
        oddArr = []
        for i in range(n):
            if nums[i] %2 ==0:
                evenArr.append(nums[i])
            else:
                oddArr.append(nums[i])
        nums = evenArr + oddArr
        return nums