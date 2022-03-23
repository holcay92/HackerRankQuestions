N = int(input())
if not 0 < N < 1000: exit("constrain")
stamps = set()
for _ in range(N):
    stamps.add(input())
print(stamps)
print(len(stamps))