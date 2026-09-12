# [Min Max Game](https://leetcode.com/problems/min-max-game/)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

**Topics:** Array, Simulation

---

You are given a **0-indexed** integer array `nums` whose length is a power of `2`.

Apply the following algorithm on `nums`:

	- Let `n` be the length of `nums`. If `n == 1`, **end** the process. Otherwise, **create** a new **0-indexed** integer array `newNums` of length `n / 2`.

	- For every **even** index `i` where `0 

```
Input: nums = [1,3,5,2,4,8,2,2]
Output: 1
Explanation: The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.
```

**Example 2:**

```
Input: nums = [3]
Output: 3
Explanation: 3 is already the last remaining number, so we return 3.
```

 

**Constraints:**

	- `1 <= nums.length <= 1024`

	- `1 <= nums[i] <= 109`

	- `nums.length` is a power of `2`.

---

*Synced automatically by **GetLeet** — inspired by [LeetSync](https://github.com/LeetSync/LeetSync), the original LeetCode → GitHub sync extension. 🙏*
