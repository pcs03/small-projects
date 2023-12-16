def merge_sort(items):
    if len(items) <= 1:
        return items

    left = []
    right = []
    for i, el in enumerate(items):
        if i < len(items) / 2:
            left.append(el)
        else:
            right.append(el)

    left = merge_sort(left)
    right = merge_sort(right)

    result = []
    print(left, right)

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend([*right, *left])

    print(left, right)
    print()
    return result


items = [0, 1, 3, 9, 8, -1, 3, 4, 5, 5, 10]

print(merge_sort(items))
