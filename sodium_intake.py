# n = int(input())
# m = int(input())
n,m = list(map(int, input().split()))

arr = list(map(int, input().split()))
total = 0
for i in range(n):
    for j in range(i, n):
        total +=arr[j]



              