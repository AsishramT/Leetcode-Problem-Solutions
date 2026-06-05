# 143. Reorder List

[143. Reorder List](https://leetcode.com/problems/reorder-list/)
Solved  
Medium

## Problem

You are given the head of a singly linked list.

The list can be represented as:

```text
L0 → L1 → … → Ln-1 → Ln
```

Reorder the list into the following form:

```text
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
```

You may not modify the values in the list's nodes. Only the node connections themselves may be changed.

---

## Example 1

```text
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

Explanation:

```text
1 → 2 → 3 → 4

becomes

1 → 4 → 2 → 3
```

---

## Example 2

```text
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

Explanation:

```text
1 → 2 → 3 → 4 → 5

becomes

1 → 5 → 2 → 4 → 3
```

---

## Constraints

- The number of nodes in the list is in the range `[1, 5 * 10^4]`
- `1 <= Node.val <= 1000`