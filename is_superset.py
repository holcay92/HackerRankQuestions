import numpy as np

A = set(map(int, input().split()))
if not 0 < len(A) < 501: exit("constrain")


n = int(input())
if not 0 < n < 21: exit("constrain")

B = list()

for i in range(0, n):
    value = set(map(int, input().split()))
    B.append(value)
   # B[i] = set(map(int, input().split()))
    if not 0 < len(B) < 101: exit("constrain")
print(len(B))
is_strict_superset = True

for i in B:
    if not i.issubset(A) and len(A) > len(i): is_strict_superset = False

print(is_strict_superset)