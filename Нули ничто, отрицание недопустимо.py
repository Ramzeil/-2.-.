my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
v = 0
list_cap = len(my_list)
while v < list_cap:
    if (my_list[v] >= 0):
        if (my_list[v] > 0):
            print(my_list[v])
        v += 1
    elif (my_list[v] < 0):
        break
