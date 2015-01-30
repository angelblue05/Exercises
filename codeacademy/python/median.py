def median(lst):
    lst = sorted(lst)
    middle = len(lst) / 2
    if len(lst) % 2 == 0:
        return (lst[middle] + lst[middle - 1]) / 2.0
    else:
        return lst[middle]
