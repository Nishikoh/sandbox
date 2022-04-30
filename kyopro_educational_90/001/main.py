import pdb

N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))

A = sorted(A)

left = 0
right = L - 1


def check(length) -> bool:
    """
    It checks if it's possible to split the array into K+1 parts, where each part is of length at most
    length

    Args:
      length: the length of the part

    Returns:
      True or False
    """

    part_length = 0
    count = 0
    for i in A:
        part_length += i
        if length <= part_length:
            count += 1
            part_length = 0

    pdb.set_trace()
    # if part_length < length:
    #     return False
    return K + 1 <= count


print(A)
# 二分探索
while left <= right:

    pdb.set_trace()
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
    print(left, right)
print(left)
