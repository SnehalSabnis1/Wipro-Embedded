def find_sum(n):
    nums = 0
    while nums < n:
        nums += 1
        yield nums

print(sum(find_sum(20)))