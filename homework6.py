my_dict = {'Ivan': 2001, 'Vasili': 2003, 'Yaroslav': 2000}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Sasha', 'none key'))
my_dict.update({'Sanya': 2004, 'Anatoly': 2001})
print(my_dict.pop('Ivan'))
print(my_dict)
my_set = {1, 3, 2, 1, True, 'Nata', False}
print(my_set)
my_set.update({54, 23})
my_set.remove(1)
print(my_set)
