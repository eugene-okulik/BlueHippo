my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [1, 2, 3, 4, 5],
           'dict': {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5'},
           'set': {1, 2, 3, 4, 5}
           }
print(my_dict['tuple'][-1])
my_dict['list'].append(6)
my_dict['list'].pop(1)
my_dict['i am a tuple'] = (5, 4, 6, 7, 11)
my_dict['dict'].pop('one', '1')
my_dict['set'].add(120)
my_dict['set'].pop()
print(my_dict)
