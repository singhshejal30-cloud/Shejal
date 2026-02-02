
# 1. creating a list
fruits=['apple','banana','cheery','mango','orange']
print("original list:",fruits)

# #2. accessing elements in a list
# first_fruit= fruits[0]      #first element
# last_fruit= fruits[-1]       #last element
# print('frist fruit:', first_fruit)
# print('last fruits:', last_fruit)

# #3. sclicing a list
# sublist_fruits= fruits[:3]
# print('sublist of first three fruits:', sublist_fruits)

# #4. adding elements to a list
# fruits.append('grapes')
# print("list after adding'grapes':", fruits)

# #5. inserting elements into a list
# fruits.insert(1, "pineapple")
# print("list after inserting 'pineapple' at position 1:", fruits)

# #6. removing elements from a list
# fruits.remove('banana')
# print("list after removing 'banana':", fruits)

# #7. popping elements from a list
# popped_fruit= fruits.pop()   #remove and returns the last item
# print('popped fruit:', popped_fruit)
# print('list after popping the last element:', fruits)

# #8. finding the length of a list
# length = len(fruits)
# print('number of fruits in the list:', length)

# #9. checking membership in a list
# is_in_list = 'apple' in fruits
# print("is 'apple' in the list?", is_in_list)

# #10. iterating over a list
# print("iterating over the list:")
# for fruit in
#  fruits:
#     print(fruit)

# #11. sorting a list
# fruits.sort()
# print("list after sorting aiphabetically:", fruits)

#12. reversing a list
fruits.reverse()
print("list after reversing the order:", fruits)

# #13. list comprehensions
# long_fruits= [fruit for fruit in fruits if len(fruit) > 5]
# print("fruits with morethan 5 letters:", long_fruits)

# #14. copying a list
# fruits_copy = fruits.copy()
# print("copied list:", fruits_copy)

# #15. clearing a list 
# fruits.clear()
# print("list after clearing all elements:", fruits)

# #16. extending a list with another list.
# vegetables = ["carrot","broccoli","spinach"]
# fruits_copy.extend(vegetables)
# print("list after extending with vegetables:", fruits_copy)

# #17. counting occurrences of an element in a list
# num_apples = fruits_copy.count("apple")
# print("number of 'apple' in the list:", num_apples)

# #18. finding the index of an element
# if"carrot" in fruits_copy:
#    carrot_index = fruits_copy.index("carrot")
#    print("index of 'carrot:", carrot_index)

# #19. removing an element by index
# if len(fruits_copy) > 2:
#     del fruits_copy[2]
# print('list after remoing element at index 2:', fruits_copy)

# #20. nested lists
# nested_list = [fruits_copy, vegetables]
# print("nested list:", nested_list)

#creating a tuple 
# my_tuple = (10,20,30,40,50,60)
# print("tuple:",my_tuple)

# #accessing elements in a tuple
# print("first element:", my_tuple[0])
# print("last element:", my_tuple[-1])

# #slicing a tuple
# print("slice[1:4]:",my_tuple[1:4])
# print("slice from brginnig to index 3:", my_tuple[:3])
# print("slice from index 2 to end:", my_tuple[2:])

# #concatetenating two tuples
# extra_tuple = (70, 80, 90)
# concatetenated = my_tuple + extra_tuple
# print("contenated tuple:", concatetenated)

# #iterating through a tuple
# for item in my_tuple:
#     print("item:", item)

# #membership test in a tuple
# print("is 30 in tuple?", 30 in my_tuple) 
# print("is 100 not in tuple?", my_tuple)

# #nested and accessing their tuple
# nested_tuple = (my_tuple, (70,80,90))
# print("nested tuple:", nested_tuple)
# print("accessing nested element (my_tuple[2]):", nested_tuple[0][2])
# print("accessing nested element (90):", nested_tuple[1][2])

# #built-in functions on tuple 
# print("length of tuple:",len(my_tuple))
# print("maximum value:", max(my_tuple))
# print("minimum value:", min(my_tuple))
# print("sum of elements:", sum(my_tuple))

# #updating a tuple (using a list conversion)
# temp_list = list(my_tuple)
# temp_list[2] = 99            #update 3rd element
# updated_tuple = tuple(temp_list)
# print("updated tuple:",updated_tuple)

# #deleting a tuple
# del my_tuple
# print(my_tuple)

# #1.creating and accessing strings
# my_string = "hello, edunet!"
# print("original string:", my_string)
# print("first character:", my_string[0])
# print("last character:", my_string[-1])

# #2.string concatenation and repetition
# str1 = "edunate"
# str2 = "foundation"
# concat_str = str1+" " +str2    #concatenation
# repeated_str = concat_str * 3
# print('concatenated string:', concat_str)
# print("repeated string:", repeated_str)

# #3. string case manipulation
# upper_str = my_string.upper()
# lower_str = my_string.lower()
# title_str = my_string.title()
# swapcase_str = my_string.swapcase()
# print("uppercase:", upper_str)
# print("lowercase:", lower_str)
# print("title case:", title_str)
# print("swap case:", swapcase_str)

# #4. searching in strings
# substring = "edunet"
# found_index = my_string.find(substring)
# if found_index != -1:
#     print(f"substring '{substring}' found at index {found_index}")
# else:
#     print(f"substring '{substring}' not found")

# #5. replacing substrings
# new_string = my_string.replace("edunet", "world")        
# print("string after replacement:", new_string)

# #6. string formatting
# name = "shejal"
# age = 25
# formatted_str = f"my name is {name} and i am {age} years old."
# print("formatted string:", formatted_str)

# #original string with extra spaces
# text = "  extra spaces  "
# #padding example (manually adding * characters)
# padded = "*** hello, edunet!***"
# print("trimmed string:", padded)
 
# #trimming example (removing leading and trailing spaces)
# trimmed = text.strip()
# print("trimmed string:", trimmed)

# #8. splitting and joining strings
# sentence = "python is fun"
# words = sentence.split()     #splitting based on spaces
# joined_sentence = '-' .join(words)    #joining with hyphen
# print("splitted words:", words)
# print("joined sentence:", joined_sentence)

# #9. counting characters
# char_count = my_string.count('o')
# print(f"character 'o' appears {char_count} times in the string")

# #10. checking string properties
# is_alpha = "hello".isalpha()
# is_digit = "12345". isdigit()
# is_alnum = "hello123".isalnum()
# is_space = "   ".isspace()
# print("is 'hello' alphabetic?", is_alpha)
# print("is '12345' numeric?", is_alnum)
# print("is 'hello123' alphanumeric?", is_alnum)
# print("is '  ' all spaces?", is_space)



# #1.creating sets
# set_a = {1,2,3,4,5}
# set_b = {4,5,6,7,8}
# print("set a:", set_a)
# print("set b:", set_b)

# #2.adding and removing elements in a set
# set_a.add(6)
# set_a.remove(1)
# print("set a:",set_a)
# print("set b:",set_b)

# #3. union of sets
# union_set = set_a.intersection(set_b)
# print("intersection of set a and set b (a - b):",union_set)

# #4. intersection0f sets
# intersection_set = set_a.intersection(set_b)
# print("intersection of a and b:", intersection_set)

# #5. difference of sets
# difference_set = set_a.difference(set_b)
# print("difference of set a and b (a - b):", difference_set)

# #6. symmetric difference of sets
# sym_diff_set = set_a.symmetric_difference(set_b)
# print("symmetric difference of set a and b:", sym_diff_set)

# #7. subset and superset testing
# set_c = {4, 5}
# is_subset = set_c. issubset(set_a)
# is_superset = set_a.issuperset(set_c)
# print(f"is set c a subset of set a?{is_subset}")

# #8. set membership testing
# is_member = 3 in set_a
# print("is 3 in set a?", is_member)

# #9. removing duplicatees using sets
# number_list = [1,2,3,4,4,5,6,6,7]
# unique_numbers = set(number_list)      #removing duplicates
# print("list of numbers after removing duplicates:", unique_numbers) 

# #set comprehension
# square_set = {x ** 2 for x in range(1,11)}
# print("set of squares of numbers from 1 to 10:", square_set)

# #clearing set
# set_a.clear()
# print("set a after clearing:", set_a)












