# Minimum Path Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

 **Note:**  You can only move either down or right at any point in time.

 

 **Example 1:** 

```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

```

 **Example 2:** 

```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200

## Solution

**Language:** Python  
**Runtime:** 10 ms (beats 61.56%)  
**Memory:** 21.2 MB (beats 84.60%)  
**Submitted:** 2026-07-11T07:58:50.334Z  

```py
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-path-sum/)