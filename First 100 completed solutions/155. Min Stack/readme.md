# 155. Min Stack

[155. Min Stack](https://leetcode.com/problems/min-stack/)
Solved
Medium
Topics
Companies

Design a stack that supports:

- `push`
- `pop`
- `top`
- `getMin`

All in **O(1)** time.

---

## Example 1

```
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```

```
Output:
[null,null,null,null,-3,null,0,-2]
```

---

## Explanation

```
push(-2)
push(0)
push(-3)

getMin() → -3
pop()
top()    → 0
getMin() → -2
```

---

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- Up to `3 * 10^4` operations
- `pop`, `top`, and `getMin` are always valid (stack not empty)