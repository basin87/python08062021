data = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
empty = [k for k, v in data.items() if not v]
for k in empty:
    del data[k]
print(data)