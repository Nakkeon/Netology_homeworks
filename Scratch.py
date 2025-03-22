N = int(input)
a = [int(x) for x in input().split()]
count = 0

for x in a:
    if x == N:
        count += 1