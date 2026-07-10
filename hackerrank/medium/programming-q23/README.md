# TwoPointerTargetCheck

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a sorted (in ascending order) integer array nums of n elements and a target value, find if there exists any pair of elements (nums[i], nums[j], i!=j) such that their sum is equal to target.

 **Solve this problem using the Two-pointers concept. The complexity should not be O(N-square) or more** 

 **Input Format** 

5
-3 -1 0 1 2
-2

 **Constraints** 

1 < nums.length <100

 **Output Format** 

Yes

 **Sample Input 0** 

```
5
-3 -1 0 1 2
-2

```

 **Sample Output 0** 

```
Yes

```

 **Sample Input 1** 

```
5
-2 0 1 1 5
0

```

 **Sample Output 1** 

```
No

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-10T06:48:11.339Z  

```py
n =  int(input())

num = list(map(int,input().split()))

target = int(input())

left = 0
right = n-1
found = False

while left<right:
    current_sum = num[left]+num[right]
    
    if current_sum == target:
        found= True
        break
    elif current_sum < target:
        left+=1
    else:
        right-=1
        
if found:
    print("Yes")
else:
    print("No")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/programming-q23/problem)