# CheckDuplicates

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array nums, print "true" if any value appears at least twice in the array, and print "false" if every element is distinct.

Read n, the number of values in the first line, followed by the n numbers in the next line.

 **Input Format** 

4 1 2 3 1

 **Constraints** 

NA

 **Output Format** 

true

 **Sample Input 0** 

```
4
1 2 3 1

```

 **Sample Output 0** 

```
true

```

 **Sample Input 1** 

```
4
1 2 3 4

```

 **Sample Output 1** 

```
false

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-10T06:47:25.650Z  

```py
n = int(input())
nums = list(map(int, input().split()))

seen =set()
duplicate = False

for num in nums:
    if num in seen:
        duplicate=True
        break
    seen.add(num)
    
if duplicate:
    print("true")
else:
    print("false")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/programming-q20/problem)