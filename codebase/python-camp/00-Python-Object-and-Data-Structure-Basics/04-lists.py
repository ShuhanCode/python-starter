
new_list = ['a', 'x', 'c']

unexpect_result = new_list.sort()

my_sorted_list = new_list

print(type(unexpect_result))

print(my_sorted_list)

new_list = ['a', 'x', 'c']

my_sorted_list = new_list = sorted(new_list)

print(my_sorted_list)