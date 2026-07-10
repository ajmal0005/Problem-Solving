# TeamRoomOfPlayers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

In this challenge, determine the minimum number of chairs needed to accommodate all cricket players in a new team relaxation room. The room does not have any chairs at the beginning.

There will be a string of simulations. A combination of four characters describes each simulation:

C, R, U, and L

• C - A new player arrives in the room. If there is a chair available, the player takes it. Otherwise, a new one is purchased.

• R - A player goes to play cricket, freeing up a chair.

• U - A player arrives at the room after playing. If there is a chair available, the player takes it. Otherwise, a new one is purchased.

• L - A player leaves the room for practice, freeing up a chair.

Example:

Given a string representing the simulations: "CRUL". In this case, the simulation is represented in the below table:

Read the string as input from the console and print the minimum number of chairs required for the simulation.

 **Input Format** 

CCCRRR

 **Constraints** 

NA

 **Output Format** 

3

 **Sample Input 0** 

```
CCCRRR

```

 **Sample Output 0** 

```
3

```

 **Sample Input 1** 

```
CCRURC

```

 **Sample Output 1** 

```
2

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-10T06:46:43.196Z  

```py
string = input().strip()

chair = 0
available =0

for ch in string:
    if ch == 'C' or ch == 'U':
        if available>0:
            available-=1
        else:
            chair +=1
    elif ch == 'R' or ch == 'L':
        available+=1
print(chair)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/programming-q19/problem)