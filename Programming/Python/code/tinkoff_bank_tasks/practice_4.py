n = int(input())
a = list(map(int, input().split()))

counts = {}
max_len = 0

for i in range(n):
    counts[a[i]] = counts.get(a[i], 0) + 1
    
    # check if prefix is boring
    freq = list(counts.values())
    freq.sort()
    if len(freq) <= 1 or (freq[-1] - freq[-2] == 1 and freq[-2] == freq[0]) or (freq[0] == 1 and freq[1] == freq[-1]):
        max_len = i + 1

print(max_len)