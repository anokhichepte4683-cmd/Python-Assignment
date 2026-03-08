set1 ={1,2,3,4,5,6}
set2 ={6,7,8,9,10}
print("Created set 1",set1)
print("Created set 2",set2)
union_set = set1|set2
print("Addition of two sets",union_set)
intersection_set = set1 & set2 
print("Intersection of two sets ",intersection_set)
difference_set = set1-set2
print("Difference of two set",difference_set)
set1.add(23)
print(set1)
set1.remove(23)
print(set1)
set1.discard(4)
print(set1)