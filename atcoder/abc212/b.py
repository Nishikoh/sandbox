code = list(input())
if len(set(code)) == 1:
    print("Weak")
else:
    is_weak = all((int(code[i]) + 1) % 10 == int(code[i + 1]) for i in range(3))
    if is_weak:
        print("Weak")

    else:
        print("Strong")
