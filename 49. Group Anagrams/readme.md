# 49. Group Anagrams

[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
Solved  
Medium

## Problem

Given an array of strings `strs`, group the anagrams together.

You may return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of another word, using all the original letters exactly once.

---

## Example 1

```text
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

Explanation:

- There is no string in `strs` that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams of each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams of each other.

---

## Example 2

```text
Input: strs = [""]

Output: [[""]]
```

---

## Example 3

```text
Input: strs = ["a"]

Output: [["a"]]
```

---

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters