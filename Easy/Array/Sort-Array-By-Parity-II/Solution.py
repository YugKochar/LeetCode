class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        evenArr = []
        oddArr = []
        result = []
        for i in range(n):
            if nums[i]%2 == 0:
                evenArr.append(nums[i])
            else:
                oddArr.append(nums[i])
        for i in range(len(evenArr)):
            result.append(evenArr[i])
            result.append(oddArr[i])
        
        return result
    