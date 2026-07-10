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
