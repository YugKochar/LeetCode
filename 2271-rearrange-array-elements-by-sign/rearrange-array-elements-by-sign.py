class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        for num in nums:
            if num>=0:
                pos.append(num)
            else:
                neg.append(num)
        n = len(nums)
        arr = [0]*n
        for i in range(n//2):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        return arr