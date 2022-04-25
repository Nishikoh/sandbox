N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))

A=sorted(A)

left = 0
right = L-1

def check(length):
    part_length = 0
    count = 0
    for i in A:
        part_length +=i
        if(length<=part_length):
            count+=1
            part_length=0                        

print(A)
