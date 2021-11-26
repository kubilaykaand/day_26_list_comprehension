name = "kubbs"
letters_list =[letter for letter in name]
range(1,5)
range_list = [num * 2  for num in range(1,5)]

#new_list = [new_item for item in list if test]
#only run the code if the test passes

names= ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

#conditional list comprehension
short_names= [name for name in names if len(name)<5]
long_names = [name.upper() for name in names if len(name)>=5]

