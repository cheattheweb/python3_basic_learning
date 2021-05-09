# identity operators
x = 10 

y = 10

z = 25

print( x != y) # print( x is y)
print( x is not z)# print ( x != y)

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list3 = [1, 2, 3]

print("1 ",list1 is list2)
print("2 ",list1 is not list2)
print("3 ",list1 == list2)
print("4 ",list == list3)

#membership operators
name = 'Arka Barua'

print("5",'A' in name)
print("6",'H' in name)
print("7",'O' not in name)