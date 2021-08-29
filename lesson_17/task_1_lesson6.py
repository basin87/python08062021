def join_var_into_dict(x: str, y: str):
    splitted_params = x.split(), y.split()
    united_dictionary = dict(zip(splitted_params[0], splitted_params[1]))
    return united_dictionary


code = "BTC"
name = "Bitcoin"
print(join_var_into_dict(name, code))