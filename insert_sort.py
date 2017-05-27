def insert_sort(lst): # 어떻게 해야하나....
    sort_lst = list()
    for i in lst:
    # for i in range(len(lst)): # Why stop!????
        iv = lst.pop(0)
        # iv = lst[i]
        if (len(sort_lst) == 0) or (sort_lst[-1] < iv):
            sort_lst.append(iv)
        else:
            for idx0, j in enumerate(sort_lst):
                if j >= iv:
                    sort_lst.insert(idx0, iv)
    return sort_lst



d = [2, 4, 5, 1, 3]
print(insert_sort(d))
