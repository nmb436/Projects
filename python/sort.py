
def bubblesort(my_list):
    for passnum in range(len(my_list)-1,0,-1):
        for i in range(passnum):
            if my_list[i]>my_list[i+1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp

my_list=[67, 45, 2, 13, 1, 998]
bubblesort(my_list)
print(my_list)

##############

def bubblesort(my_list_two):
    for passnum in range(len(my_list_two)-1,0,-1):
        for i in range(passnum):
            if my_list_two[i]>my_list_two[i+1]:
                temp = my_list_two[i]
                my_list_two[i] = my_list_two[i + 1]
                my_list_two[i + 1] = temp

my_list_two=[89, 23, 33, 45, 10, 12, 45, 45, 45]
bubblesort(my_list_two)
print(my_list_two)
