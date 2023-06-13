first_name = 'Melissa'
last_name = 'Williamson'
# these are giving the values for the dictionary class further down the page.

full_name = first_name + last_name
print(full_name)
# gives the full name but like its one word

# the '' in this line signifies a space between the names.
full_name_with_space = first_name + ' ' + last_name
print(full_name_with_space)

name_list = ['Melissa', 'Williamson']
print(name_list)

first_name_list = [first_name]
last_name_list = [last_name]
print(first_name_list)
print(type(first_name_list))
print(last_name_list)
print(type(last_name_list))

# dictionary is a type of list
name_dictionary = {'first': first_name_list, 'last': last_name_list}
print(name_dictionary)
print(type(name_dictionary))





