def changes(some_string, previous_item, desired_item, times_of_repeat):
    return some_string.replace(previous_item, desired_item, times_of_repeat)


print(changes('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))