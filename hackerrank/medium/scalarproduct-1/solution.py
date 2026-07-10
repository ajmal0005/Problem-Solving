n = int(input())

v1 = list(map(int,input().split()))
v2 = list(map(int,input().split()))

v1.sort()
v2.sort(reverse=True)

scalar_multiply = 0

for i in range(n):
    scalar_multiply+= v1[i]*v2[i]

print(scalar_multiply)
