my_list = [1,2,3,4,5,6]
print("Created list is :",my_list)
my_list.append(10)
print("List after appending element",my_list)
my_list.extend([12,13])
print("List after extending element:",my_list)
my_list.insert(2,'23')
print("List after inserting an element",my_list)


my_list.remove(4)
print("List after removing an element ",my_list )
my_list.pop()
print("List after popping:",my_list)
my_list.clear()
print("List after clearing ",my_list)

my_list = [1, 2, 23, 3, 5, 6, 10, 12]
my_list[3]= 44
print("List after modifying ",my_list)


my_list.sort()
print("List after sorting", my_list)
my_list.sort(reverse=True)
print("List in descending order:",my_list)
sorted_list =sorted(my_list)
print("Sorted list is ",my_list)


my_list.reverse()
print("List after reversing :",my_list)
reversed_list = list(reversed(my_list))
print("Reversed list",reversed_list)