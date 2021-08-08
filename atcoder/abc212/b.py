code = list(input())
if len(set(code)) == 1:
    print("Weak")
else:
    is_weak = True
    for i in range(3):
        if (int(code[i]) + 1) % 10 != int(code[i + 1]):
            is_weak = False

    if is_weak:
        print("Weak")

    else:
        print("Strong")
