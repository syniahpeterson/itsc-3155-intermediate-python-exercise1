# Syniah Peterson

# Creates a function that combines the dictionaries and outputs the combined dictionary
def get_combined_dict(dict1, dict2):
    dict3 = dict(dict1)
    dict3.update(dict2)
    for i, j in dict1.items():
        for x, y in dict2.items():
            if i == x:
                dict3[i] = (j + y)
    return dict3

my_dict1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict1, my_dict2)
print(combined_dict)