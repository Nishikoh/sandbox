n, m = map(int, input().split())
node = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    node[a - 1].append(b - 1)
    node[b - 1].append(a - 1)
linked_node = set()
linked_node |= set(node[0])
add_node = set()
for start in linked_node:
    add_node |= set(node[start])
if n - 1 in add_node:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
# print(node)
# print((add_node))
