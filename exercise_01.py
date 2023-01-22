# Syniah Peterson

# Function that returns one of every element in the list
def get_unique_list(list):
    unique = []
    duplicate = []
    for i in list:
        if i not in unique:
            unique.append(i)
        else:
            duplicate.append(i)
    return unique

# Populates the outputs the list with one of every element in it
my_list = [10, 2, 30, 2, 1, 4, 4, 4, 1, 16]
unique_list = get_unique_list(my_list)
print("The unique numbers are: " + str(unique_list))