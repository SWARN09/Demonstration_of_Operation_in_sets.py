#progarm to demonstate operations in sets in python
#length
#remove
#pop
#clear
#union
#intersection

#consider the following set for this example
s = {1,2,3,4,'a','b','c','d'}
print(type(s))

#this will print lenght of sets; number of elements present in the sets
print(len(s))

#this will print a new sets which is union of above and below set
print(s.union({5,6,'e','f'}))

#this will print a new sets which is intersection of above and below set
print(s.intersection({1,2,'a','b'}))

#this will remove the element of the set which you instruct
s.remove(4)
print(len(s))

#this will remove the element of the set arbitiary
s.pop()
print(len(s))

#this will empty the given set;len = 0
s.clear()
print(len(s))