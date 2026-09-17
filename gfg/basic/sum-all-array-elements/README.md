# Sum of Array

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an integer array  **arr[]**, return the sum of all elements of arr.

 **Examples:** 

```
Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.

```

```
Input: arr[] = [1, 3, 3]
Output: 7
Explanation: 1 + 3 + 3 = 7.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-17T17:10:43.025Z  

```py
class Solution:
    def arraySum(self, arr):
        total = 0

        for i in arr:
            total = total + i

        return total
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sum-all-array-elements/1)