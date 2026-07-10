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
