# BuySellStocks

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program that takes an array that denotes the daily closing prices of a stock to determine the maximum profit by buying and selling one share of the stock.

 **Input Format** 

9
310 315 275 260 270 290 230 255 250

 **Constraints** 

NA

 **Output Format** 

30

 **Sample Input 0** 

```
9
310 315 275 260 270 290 230 255 250

```

 **Sample Output 0** 

```
30

```

 **Explanation 0** 

Buy at 260, Sell at 290

 **Sample Input 1** 

```
4
1 2 3 4

```

 **Sample Output 1** 

```
3

```

 **Explanation 1** 

Buy at 1, Sell at 4

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-10T06:40:48.813Z  

```py
n = int(input())
prices = list(map(int, input().split()))

min_price = prices[0]
max_profit = 0

for i in range(1, n):
    profit = prices[i] - min_price
    if profit > max_profit:
        max_profit = profit
    if prices[i] < min_price:
        min_price = prices[i]

print(max_profit)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/programming-q24/problem)