def purify(lst):
    mod_list = []
    for num in lst:
        if num % 2 == 0:
            mod_list.append(num)
    return mod_list
