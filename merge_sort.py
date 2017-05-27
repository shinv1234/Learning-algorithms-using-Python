def merge_sort(a, b): # 아아아아아아!!!! 외않되?????!!!!
    sort_lst = list()
    i = 0; j = 0
    while i < len(a) or j < len(b):
        if a[i] >= b[j]:
            sort_lst.append(b[j])
            print(sort_lst)
            j += 1
        else:
            sort_lst.append(a[i])
            print(sort_lst)
            i += 1
    if len(a) < i:
        sort_lst += b[j:]
    elif len(b) < j:
        sort_lst += a[i:]
    return sort_lst

a = [0, 2, 5, 7, 8]
b = [1, 3, 4, 6, 9, 10]

'''a = [1, 3, 5, 7, 9]
b = [0, 2, 4, 6, 8]'''

print(merge_sort(a, b))
