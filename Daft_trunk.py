# n = int(input())
# arr=[]

# num = list(map(int, input().split()))
# count = 0
# for i in range(1,len(num)):
#     if num[i] < num[i-1]:
#         count +=1
# replacement_count = int(count//2)
# print(replacement_count)


n = int(input())
a = list(map(int, input().split()))

count = 0
i = 0

while i < n - 2:
    if a[i] > a[i + 1]:
        length = 0

        while i < n - 1 and a[i] > a[i + 1]:
            length += 1
            i += 1
        count += length // 2
    else:
        i += 1

print(count)

