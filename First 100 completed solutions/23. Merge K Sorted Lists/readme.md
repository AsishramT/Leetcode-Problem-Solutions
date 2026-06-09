# 23. Merge k Sorted Lists

[23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
Solved
Hard
Topics
Companies

You are given an array of `k` linked lists, each sorted in ascending order.

Merge all the linked lists into one sorted linked list and return it.

---

## Example 1:

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
``` id="a1b2c3"

Explanation:
```
1->4->5,
1->3->4,
2->6
```

Merged into:
```
1->1->2->3->4->4->5->6
```

---

## Example 2:

```
Input: lists = []
Output: []
``` id="d4e5f6"

---

## Example 3:

```
Input: lists = [[]]
Output: []
``` id="g7h8i9"

---

## Constraints:

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- Each list is sorted in ascending order
- Total number of nodes ≤ `10^4`
```