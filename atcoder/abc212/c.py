n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b)
ans = 1e9
b_i = 0
for a_i in a:
    for i in range(b_i, len(b)):
        if abs(a_i - b[i]) <= ans:
            b_i = i
            ans = min(ans, abs(a_i - b[i]))
        else:
            break
print(ans)
