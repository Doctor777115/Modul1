my_dict = {'Alex': 1996, 'Masha': 2000, 'Julia': 1992}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Andrey'))
my_dict.update({'Max': 1988,
               'Olga': 1956})
print(my_dict.pop('Masha'))
print(my_dict)

my_set = {1, 2, 3, 1, 2, 3, 4, 5, 6, 'string', 9, 9, 'string'}
print(my_set)
my_set.update({'Olga',7})
print(my_set)
my_set.discard(7)
print(my_set)