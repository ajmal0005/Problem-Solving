# Running Time of Algorithms

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

In a previous challenge you implemented the _Insertion Sort_ algorithm. It is a simple sorting algorithm that works well with small or mostly sorted data. However, it takes a long time to sort large unsorted data. To see why, we will analyze its running time.

**Running Time of Algorithms**  
The running time of an algorithm for a specific input depends on the number of operations executed. The greater the number of operations, the longer the running time of an algorithm. We usually want to know how many operations an algorithm will execute in proportion to the size of its input, which we will call $N$.

What is the ratio of the running time of Insertion Sort to the size of the input? To answer this question, we need to examine the algorithm. 

**Analysis of Insertion Sort**  
For each element $V$ in an array of $N$ numbers, Insertion Sort compares the number to those to its left until it reaches a lower value element or the start.  At that point it shifts everything to the right up one and inserts $V$ into the array. 

How long does all that shifting take?

In the best case, where the array was already sorted, no element will need to be moved, so the algorithm will just run through the array once and return the sorted array. The running time would be directly proportional to the size of the input, so we can say it will take $N$ time.

However, we usually focus on the worst-case running time (computer scientists are pretty pessimistic). The worst case for Insertion Sort occurs when the array is in reverse order. To insert each number, the algorithm will have to shift over that number to the beginning of the array. Sorting the entire array of $N$ numbers will therefore take $1+2+...+(N-1)$ operations, which is $N(N-1)/2$ (almost $N$<sup>$2$</sup>$/2$). Computer scientists just round that up (pick the dominant term) to $N$<sup>$2$</sup> and say that Insertion Sort is an "$N$<sup>$2$</sup> time" algorithm.

![running-time-picture](https://s3.amazonaws.com/hr-challenge-images/insertion-sort/InsertionSortRunningTime-small.png)

**What this means**  
The running time of the algorithm against an array of $N$ elements is $N$<sup>$2$</sup>. For $2N$ elements, it will be $4N$<sup>$2$</sup>.  Insertion Sort can work well for small inputs or if you know the data is likely to be nearly sorted, like check numbers as they are received by a bank.  The running time becomes unreasonable for larger inputs. 

----

**Challenge**  
Can you modify your previous Insertion Sort implementation to keep track of the number of shifts it makes while sorting? The only thing you should print is the number of shifts made by the algorithm to completely sort the array. A shift occurs when an element's position changes in the array. Do not shift an element if it is not necessary.

**Function Description**

Complete the *runningTime* function in the editor below.   

runningTime has the following parameter(s):  

- *int arr[n]:* an array of integers   

**Returns**   

- *int:* the number of shifts it will take to sort the array   

**Input Format**

The first line contains the integer $n$, the number of elements to be sorted.  
The next line contains $n$ integers of $arr[arr[0] \ldots arr[n-1]]$. 

**Constraints**

$1 \le n \le 1001$   
$-10000 \le a[i] \le 10000, \text{ where } i \in \{0..(n-1)\}$
 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T05:38:58.330Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1

        arr[j + 1] = key

    return shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/runningtime/problem)