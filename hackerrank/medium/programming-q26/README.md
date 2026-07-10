# CountNegativesAmazon

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

**Solve this problem with a complexity less than m+n.** 

Read the following input: an integer n representing the number of rows in the matrix, and an integer m representing the number of columns in the matrix and the values of the matrix (n rows and m columns).

The matrix is sorted such that all elements in any row are sorted in increasing order from left to right, and all elements in any column are sorted in increasing order from top to bottom. You should print the total number of negative numbers present in the matrix.

The input will be provided as follows:

- The first line of input contains a single integer n, the number of rows in the matrix.
- The second line of input contains a single integer m, the number of columns in the matrix.
- The next n lines each contain m integers separated by spaces, representing the elements of the matrix.

 **Solve this problem with a complexity less than m+n.** 

 **Input Format** 

3
4
-4 -3 -1 1
-2 -2 1 3
-1 1 2 4

 **Constraints** 

- The number of rows n and columns m will not exceed 100.
- Each row and column of the matrix is sorted in non-decreasing order.
- Matrix elements are integers.

 **Output Format** 

6

 **Sample Input 0** 

```
3
4
-4 -3 -1 1
-2 -2 1 3
-1 1 2 4

```

 **Sample Output 0** 

```
6

```

 **Sample Input 1** 

```
4
4
-7 -3 -1 4
-5 -2 2 6
-1 1 3 7
1 5 9 11

```

 **Sample Output 1** 

```
6

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-10T06:45:29.929Z  

```py
n = int(input())
m = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

row = 0
col = m-1
count = 0

while row < n and col >=0:
    if matrix[row][col]<0:
        count+=col+1
        row+=1
    else:
        col-=1
print(count)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/programming-q26/problem)