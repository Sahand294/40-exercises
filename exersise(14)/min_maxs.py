def min_max(nums):
    a = []
    a.append(min(nums))
    a.append(max(nums))
    return(tuple(a))
numbers = [5, 1, 9, 3]
print(min_max(numbers))