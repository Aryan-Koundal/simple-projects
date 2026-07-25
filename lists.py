my_list = [1,2,2,3,4,5,6,7,8,9,10]
#print list elements
for i in my_list:
    print(i)

#check wheather there is 3 in list
if 3 in my_list:
    print ("yes")
else :
    print ("no")

#append list
my_list.append(11)
print (my_list)

#insert element at idx
my_list.insert(1,"hello")
print (my_list)

#pop an element
1 == my_list.pop(1)
print (1)
print (my_list) 

#remove element
2== my_list.remove(2)
print (2)
print(my_list) 

#reverse list
my_list.reverse()
print (my_list)

#sort list 
new_list = [9,4,1,10,6,7,5,3,8,2]
new_list.sort()
print (new_list)

#add both lists
new_list1 = my_list+new_list
print (new_list1)

#megre both lists
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8,9,0]
merge = list(set(list1+list2))
print (merge)

merged1 = []
for items in list1+list2:
    if items not in merged1 :
        merged1.append(items)
print (merged1)

#slicing
my_list1 = [1,2,3,4,5,6,7,8,9,10]
a = my_list1[1:5]
print (a)
b = my_list1[1::5]
print(b)

#copy list
list3 = [1,2,3,4,5,6,7,8,9,0]
list4 = list3.copy()
print (list4)

#get square of each element in the list without compreshion
list5 = [1,2,3,4,5,6,7,8,9,0]
list6 = []
for i in list5:
 i = i*i
 list6.append(i)
print (list6)

#get square of each element in the list with compreshion
list7 = [1,2,3,4,5,6,7,8,9,0]
list8 = [i*i for i in list7]
print (list8)