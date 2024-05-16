def binary_search(sort_list, value):
    ResultOk = False
    First = 0
    Last = len(sort_list) - 1

    while First <= Last:
        Middle = (First + Last) // 2
        if value == sort_list[Middle]:
            ResultOk = True
            Pos = Middle
            break
        elif value > sort_list[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk == True:
        print("Элемент найден на позиции:", Pos)
    else:
        print("Элемент не найден")
