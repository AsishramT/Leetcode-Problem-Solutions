# 2144. Minimum Cost of Buying Candies With Discount

[2144. Minimum Cost of Buying Candies With Discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/)
Solved
Easy
Topics
Companies

A shop is selling candies at a discount. For every two candies bought, the shop gives a third candy for free.

The customer can choose any candy to take away for free as long as the cost of the chosen candy is **less than or equal to the minimum cost of the two candies bought**.

Return the minimum cost to buy all candies.

---

## Example 1:

```
Input: cost = [1,2,3]
Output: 5
```

Explanation:
We buy candies with costs 2 and 3, and take 1 for free.

---

## Example 2:

```
Input: cost = [6,5,7,9,2,2]
Output: 23
```

Explanation:
- Buy 9 and 7 → take 6 for free  
- Buy 5 and 2  
- Take last 2 for free  

---

## Example 3:

```
Input: cost = [5,5]
Output: 10
```

Explanation:
Only two candies exist, so both must be paid for.

---

## Constraints:

- `1 <= cost.length <= 100`
- `1 <= cost[i] <= 100`
```