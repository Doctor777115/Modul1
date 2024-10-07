immutable_var = (1, 2, 3, 'strint')
print(immutable_var)
print(immutable_var[0]) # вытащить объект из кортежа можно, изменить нельзя (объяснение согласно запросу задания ниже)
#immutable_var[0] = 100 # TypeError: 'tuple' object does not support item assignment (кортеж не поддерживает обращение по элементам)


muttable_list = [1,2,3,4, 'pork']
muttable_list.append('list')
print(muttable_list)
muttable_list.extend('tayota')
print(muttable_list)
muttable_list.remove('pork')
print(muttable_list)

