my_dict = {"name":"Aliyana","age":70,"country":"Japan"}
print(my_dict['name'])
my_dict['mothertongue'] = "Japanese"
print(my_dict)
my_dict['age'] = 19
print(my_dict)
my_dict.pop('country')
print(my_dict)
del my_dict['name']
print(my_dict)
my_dict.clear()
print(my_dict)

my_dict1 = {"name":"Aliyana","age":70,"country":"Japan"}
my_dict2 = {"name2":"Aila Chan ","age2":15,"country2":"Japan"}
my_dict1.update(my_dict2)
print(my_dict1)
merged_dict = my_dict1|my_dict2
print(merged_dict)