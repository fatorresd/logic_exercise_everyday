def two_sum(array, target):
    seen = {}
    for index, num in enumerate(array):
        diff = target - num
        if diff in seen:
            return [seen[diff], index]
        seen[num] = index
    return []

a = [3,2,4]
t = 6

print(two_sum(a, t))