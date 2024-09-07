my_dyct={'Andrey': 2021, 'Sergey': 2011, 'Sveta': 2005}
print(my_dyct)
print(my_dyct['Andrey'])
print(my_dyct.get('Alex', 'Такого клиента нет'))
my_dyct.update({'Roma': 2013, 'Gena': 1996})
a=my_dyct.pop('Andrey')
print(a)
print(my_dyct)
my_set={'Lena', 25, 'Kolokol', 1998, 25, 'Lena', 25, (1, 2, 3)}
print(my_set)
my_set.add(20000)
my_set.add('Boris')
print(my_set)
