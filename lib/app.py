s = [4, 6, 3, 9, 3, 5, 1, 2]
print(1 in s)


my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]

# We can define a function for the list to sort by the second key

def sort_tuple(tuple_value):

    # return the key we want to sort by
    return tuple_value[0]

my_list.sort(key = sort_tuple)
print(my_list)
# => [('Steve', 1), ('John', 2), ('Joe', 3)]

my_list = ['a', 'b', 'c', 'd', 'f']
my_list.insert(4, 'e')
print(my_list)
# => ['a', 'b', 'c', 'd', 'e', 'f']
my_list.insert(1000, 'g')
print(my_list)
# => ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(my_list.index('g'))