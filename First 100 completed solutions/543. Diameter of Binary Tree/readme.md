# 543. Diameter of Binary Tree

[543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
Solved  
Easy

## Problem

Given the root of a binary tree, return the **length of the diameter** of the tree.

The diameter of a binary tree is the **longest path between any two nodes** in the tree. This path:

- May or may not pass through the root
- Is measured in **number of edges**

---

## Example 1

```text
Input: root = [1,2,3,4,5]
Output: 3
```

Explanation:

The longest path is:

```
[4,2,1,3]
```

or

```
[5,2,1,3]
```

which has 3 edges.

---

## Example 2

```text
Input: root = [1,2]
Output: 1
```

---

## Constraints

- The number of nodes is in the range `[1, 10^4]`
- `-100 <= Node.val <= 100`