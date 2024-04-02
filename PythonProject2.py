'''
Submit a github repo link for the assignment below

Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.
'''
my_list = []
print(my_list)
my_list.extend([10,20,30,40])
print(my_list)
my_list.insert(1,15)
print(my_list)
my_list.extend([50,60,70])
print(my_list)
my_list.pop()
print(my_list)
my_list.sort()
print(my_list)
index = my_list.index(30)
print(index)


