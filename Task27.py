def list_func():
    list_ = [10, 45, 85, 12, 46, 78]
    lst_2 = []
    list_3 = []
    for i in list_:
        if i % 2 == 0:
            lst_2.append(i)
        elif i % 2 != 0:
            list_3.append(i)
    print(f"Список четных чисел {lst_2} ")
    print(f"Список четных чисел {list_3} ")
list_func()