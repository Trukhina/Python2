# Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами, 
# выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!

import random
def first_list(n):
    list = n[:]
    list_length = len(list)
    for i in range(list_length):
        index_a = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_a]
        list[index_a] = temp
    return list
list = [4, 5, 2, 8, 9]
second_list = first_list(list)
print("первый список: ")
print(list)
print("второй список - смешанный: ")
print(second_list)