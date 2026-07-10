n = int(input())
count = 0
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        count+=1
if count >0:
    print("Odd Elements:",count)
else:
    print("No odd elements are present")
