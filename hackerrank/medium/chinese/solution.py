n = int(input())

day = list(map(int,input().split()))
night = list(map(int,input().split()))

x = int(input())
pay = 0
day.sort()
night.sort(reverse=True)

for i in range(n):
    work_time = day[i]+night[i]
    if work_time > x:
        pay += (work_time-x)*100
    
print(pay)
