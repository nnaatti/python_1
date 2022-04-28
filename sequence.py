# list is an ordered sequence of items. most used datatypes

list_of_numbers = [1,2,3,4,9,99,354]

print(len(list_of_numbers))

list_of_numbers[4] = 5
print(list_of_numbers)
list_of_numbers[2] = 4
print(list_of_numbers)


#print(len(list_of_numbers))
#print(list_of_numbers[2])
#print(list_of_numbers[2:4])
#list_of_numbers.append(26)
#print(list_of_numbers)

# tuple is an ordered sequence of items same as listy=
# the only diffrence is tuples are  immutable

tuple_of_numbers = (1,2,3,4,5,6)
print(tuple_of_numbers)

# a set is unoredered collection of unique items

a_set_of_numbers = {1,2,3,4,5,6,5,7,8,1,2,3,4}
print(a_set_of_numbers)

#dictionary is unoredered collection of key and value

number_dict = {'name':'nati','sex':'male'}

print(number_dict['name'])