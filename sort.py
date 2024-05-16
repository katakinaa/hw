def bubble_sort(sort_list):
    n = len(sort_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
                swapped = True
        if not swapped:
            break
    return sort_list
