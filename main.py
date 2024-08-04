import itertools as it
k, m = map(int, input().split(' '))

k_lists = []

for k in range(k):
    k_lists.append(list(map(lambda x: x**2, list(map(int, input().split(' ')))[1:])))

print(max([sum(i) % m for i in it.product(*k_lists)]))