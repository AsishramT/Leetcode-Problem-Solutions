# 100. Same Tree

[100. Same Tree](https://leetcode.com/problems/same-tree/)
Solved  
Easy

## Problem

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are:

- Structurally identical
- Have the same node values in corresponding positions

Return `true` if the trees are the same, otherwise return `false`.

---

## Example 1

```text
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

---

## Example 2

```text
Input: p = [1,2], q = [1,null,2]
Output: false
```

---

## Example 3

```text
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

---

## Constraints

- The number of nodes in both trees is in the range `[0, 100]`
- `-10^4 <= Node.val <= 10^4`