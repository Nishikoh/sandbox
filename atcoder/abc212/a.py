a, b = map(int, input().split())
if 0 < a:
    if b == 0:
        print("Gold")
    else:
        print("Alloy")
else:
    print("Silver")
