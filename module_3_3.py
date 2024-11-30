def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = ['Hello', 123.22, False]
values_dict = {'a': 23, 'b':'World', 'c': False }
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['Name', 69.32]
print_params(*values_list_2, 42)