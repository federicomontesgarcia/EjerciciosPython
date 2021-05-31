key_list = ['name', 'age', 'address']
value_list = ['Johnny', '27', 'New York']

dict_from_list = {key_list[i]: value_list[i] for i in range(len(key_list))}
print(dict_from_list)