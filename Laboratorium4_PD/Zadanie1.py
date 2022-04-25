"""
Program creates list of given lenght where every 3rd element is a word 'fuzz'
Then user chooses one of the elements starting from the last
so if user chooses 5 from the list of 5 elements he will recive number 1
"""


def createa_and_modify_table(n):
    #wykorzystuje funkcje z zadania pierwszego z laboratoriów
    n = int(n)
    my_list = [*range(1, n+1)]
    my_list[2::3] = ["fuzz"]* (n // 3)
    return my_list


def input_correct(k, list_length):
    if not k.isdigit():
        return False
    return int(k) > 0 and int(k) <= list_length


def get_kth_elem(elems):
    k = input('Podaj k: ')
    if not input_correct(k, len(elems)):
        print("Podałeś błędną wartość!")
        return get_kth_elem(elems)
    else:
        return elems[-int(k)]


n = input("Podaj długość listy ")
my_list = createa_and_modify_table(n)
print(get_kth_elem(my_list))