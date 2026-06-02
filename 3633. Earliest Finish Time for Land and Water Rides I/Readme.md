# 3633. Earliest Finish Time for Land and Water Rides I

[3633. Earliest Finish Time for Land and Water Rides I](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/)
Solved
Easy
Topics
Companies
Hint

You are given two categories of theme park attractions: **land rides** and **water rides**.

### Land rides
- `landStartTime[i]` – the earliest time the `i`th land ride can be boarded.
- `landDuration[i]` – how long the `i`th land ride lasts.

### Water rides
- `waterStartTime[j]` – the earliest time the `j`th water ride can be boarded.
- `waterDuration[j]` – how long the `j`th water ride lasts.

A tourist must experience exactly **one ride from each category**, in **either order**.

A ride may be started at its opening time or any later moment.

If a ride is started at time `t`, it finishes at time `t + duration`.

Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

Return the earliest possible time at which the tourist can finish both rides.

---

## Example 1

```text
Input:
landStartTime = [2,8]
landDuration = [4,1]
waterStartTime = [6]
waterDuration = [3]

Output:
9
```

### Explanation

Plan A (land ride 0 → water ride 0):

```text
Start land ride 0 at time 2.
Finish at 2 + 4 = 6.

Water ride 0 opens at time 6.
Start immediately at 6.
Finish at 6 + 3 = 9.
```

Plan B (water ride 0 → land ride 1):

```text
Start water ride 0 at time 6.
Finish at 6 + 3 = 9.

Land ride 1 opens at time 8.
Start at time 9.
Finish at 9 + 1 = 10.
```

Plan C (land ride 1 → water ride 0):

```text
Start land ride 1 at time 8.
Finish at 8 + 1 = 9.

Water ride 0 is already open.
Start at time 9.
Finish at 9 + 3 = 12.
```

Plan D (water ride 0 → land ride 0):

```text
Start water ride 0 at time 6.
Finish at 6 + 3 = 9.

Land ride 0 is already open.
Start at time 9.
Finish at 9 + 4 = 13.
```

Plan A gives the earliest finish time of `9`.

---

## Example 2

```text
Input:
landStartTime = [5]
landDuration = [3]
waterStartTime = [1]
waterDuration = [10]

Output:
14
```

### Explanation

Plan A (water ride 0 → land ride 0):

```text
Start water ride 0 at time 1.
Finish at 1 + 10 = 11.

Land ride 0 opens at time 5.
Start immediately at 11.
Finish at 11 + 3 = 14.
```

Plan B (land ride 0 → water ride 0):

```text
Start land ride 0 at time 5.
Finish at 5 + 3 = 8.

Water ride 0 is already open.
Start immediately at 8.
Finish at 8 + 10 = 18.
```

Plan A provides the earliest finish time of `14`.

---

## Constraints

- `1 <= n, m <= 100`
- `landStartTime.length == landDuration.length == n`
- `waterStartTime.length == waterDuration.length == m`
- `1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1000`