n, x = map(int, input().split())
a = list(map(int, input().split()))
x = format(x, "b").zfill(len(a))
ans = sum([a[i] * int(x[-i - 1]) for i in range(n)])
print(ans)

