# 33. Search in Rotated Sorted Array

[33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
Solved
Medium
Topics
Companies

There is an integer array `nums` sorted in ascending order (with distinct values).

Before being passed to your function, `nums` is possibly rotated at an unknown index `k` such that:

```
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
```

Given the rotated array and an integer `target`, return the index of `target` if it exists, otherwise return `-1`.

You must solve it in **O(log n)** time.

---

## Example 1

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

---

## Example 2

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

---

## Example 3

```
Input: nums = [1], target = 0
Output: -1
```

---

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i], target <= 10^4`
- All values in `nums` are unique
- Array is sorted and possibly rotated
```