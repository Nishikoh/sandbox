n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
mod = 1e9 + 7
ans = a[0] + 1
for i in range(n-1):
    ans *= a[i+1] - a[i] + 1
    ans %= mod 
print(int(ans))