class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # n = len(nums)
        # st = set()
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 triplets = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 st.add(triplets)
        # return[list(triplets)for triplets in st]
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n):
            hashset = set()
            for j in range(i+1, n):
                t = -(nums[i]+nums[j])
                if t in hashset:
                    ans.add((nums[i], t,nums[j]))
                hashset.add(nums[j])
        return[list(x)for x in ans]