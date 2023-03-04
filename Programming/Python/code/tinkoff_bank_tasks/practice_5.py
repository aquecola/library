n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + a[i]

count = {}
for i in range(n+1):
    if prefix_sum[i] in count:
        count[prefix_sum[i]] += 1
    else:
        count[prefix_sum[i]] = 1

result = 0
for v in count.values():
    result += v * (v - 1) // 2

print(result)
