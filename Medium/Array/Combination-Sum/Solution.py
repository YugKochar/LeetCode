class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backTrack(start, curr, total):
            if total == target:
                ans.append(curr[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backTrack(i, curr, total+candidates[i])
                curr.pop()
        backTrack(0,[],0)
        return ans