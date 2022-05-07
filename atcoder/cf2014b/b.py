n = list(map(int, input()))
is_swap = n[-1] % 2
sum_a = sum(n[i] for i in range(0, len(n), 2))
sum_b = sum(n[i] for i in range(1, len(n), 2))
if is_swap:
    sum_a, sum_b = sum_b, sum_a
print(sum_a, sum_b)
