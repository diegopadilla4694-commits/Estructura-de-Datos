my_tuple = (2, 3)
temp_list = list(my_tuple)    # list en una funcion que te perermite crear tuplas a listas
temp_list.append(temp_list[1] + temp_list[0]) #tuple es una funcion que permite crear listas a tuplas :)

my_tuple = tuple(temp_list)

print(my_tuple)


