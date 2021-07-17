def matchvalue(x):
    keys = enumerate(list_index)
    my_dictionary = dict((key, value) for key, value in keys)
    return my_dictionary

list_index = ['a', 'b', 'c', 'd', 'e']
print(matchvalue(list_index))