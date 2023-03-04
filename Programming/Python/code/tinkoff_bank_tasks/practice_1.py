h1, h2, h3, h4 = map(int, input().split())

if h1 <= h2 <= h3 <= h4 or h1 >= h2 >= h3 >= h4:
    print("YES")
else:
    print("NO")