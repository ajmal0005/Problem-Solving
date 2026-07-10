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
