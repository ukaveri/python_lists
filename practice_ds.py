
'''
list containing values multiple values
list = [1,2,3,"kaveri"]
print(list)
...........................................
#creating list with multiple values
list1 = ["hi","i","am","kaveri"]
print("list 1 : ")
print(list1)
#multi-dimensional list
list2 = [["Nandini"],["is","my friend"]]
print("list 2 : ")
print(list2)
#accessing elements
print("First list")
print(list1[0])
print(list1[-1])
print("Second list")
print(list2[0])
print("Negative indices")
print(list2[-1])
print(list2[-2])
print("Accessing multi-dimensional lists : ")
print(list2[0][0])
print(list2[1][0])
print(list2[1][1])
list1 = [10,20,30]
print(len(list1))
print(len(list2))
print("length of list2")
print(len(list2[0]))
print(len(list2[1]))
#Naive method
#finding the length of a list using naaive method:
list1 = [10,20,30,40,50]
print("The list is : ",str(list1))
cnt =0
for i in list1:
    cnt = cnt+1
print("Length of the list is : ",cnt)
#now we can also concatinate the value to a string
#in a print statement in two ways
#i.e., print("..",+str(var))
# or   print("..",var)
list1 = [10,20,30]
list_len = sum(list1)
print(list_len)
'''
list1 = [10,20,30]
list1.append(40)
#print(list1.append(40))
print(list1)
list2 = ["nandini","kaveri","dillu"]
#list1.append(list2)
#print(list1)
for i in list2:
    list1.append(list2[i])
#print(list1)
