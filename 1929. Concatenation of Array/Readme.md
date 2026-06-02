# 1929. Concatenation of Array

[1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)
Solved
Easy
Topics
Companies

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where:

- `ans[i] == nums[i]`
- `ans[i + n] == nums[i]` for `0 <= i < n`

In other words, `ans` is the concatenation of two `nums` arrays.

---

## Example 1:

```
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
``` id="a1b2c3"

Explanation:
```
ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]
```

---

## Example 2:

```
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
``` id="d4e5f6"

Explanation:
```
ans = [nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]
```

---

## Constraints:

- `n == nums.length`
- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`