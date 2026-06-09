# 167. Two Sum II - Input Array Is Sorted

[167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
Solved  
Medium

## Problem

Given a **1-indexed** array of integers `numbers` that is sorted in non-decreasing order, find two numbers such that they add up to a specific `target`.

Let these two numbers be:

```text
numbers[index1] + numbers[index2] == target
```

where:

```text
1 <= index1 < index2 <= numbers.length
```

Return the indices of the two numbers as:

```text
[index1, index2]
```

The tests are generated such that there is **exactly one solution**, and you may not use the same element twice.

Your solution must use only **constant extra space**.

---

## Example 1

```text
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
```

Explanation:

```text
2 + 7 = 9
```

Therefore:

```text
index1 = 1
index2 = 2
```

---

## Example 2

```text
Input: numbers = [2,3,4], target = 6
Output: [1,3]
```

Explanation:

```text
2 + 4 = 6
```

Therefore:

```text
index1 = 1
index2 = 3
```

---

## Example 3

```text
Input: numbers = [-1,0], target = -1
Output: [1,2]
```

Explanation:

```text
-1 + 0 = -1
```

Therefore:

```text
index1 = 1
index2 = 2
```

---

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order
- `-1000 <= target <= 1000`
- Exactly one valid solution exists