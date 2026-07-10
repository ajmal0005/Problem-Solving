# AnagramCheck

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings s and t, print "true" if t is an anagram of s, and "false" otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 **Input Format** 

anagram
nagaram

 **Constraints** 

NA

 **Output Format** 

true

 **Sample Input 0** 

```
anagram
nagaram

```

 **Sample Output 0** 

```
true

```

 **Sample Input 1** 

```
rat
car

```

 **Sample Output 1** 

```
false

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-10T06:47:45.400Z  

```py
s= input()
t= input()

if sorted(s) == sorted(t):
    print("true")
else:
    print("false")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/programming-q21/problem)