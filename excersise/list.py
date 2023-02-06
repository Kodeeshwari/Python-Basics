'''
    topic : List

'''

list1 = [12,23.4,'kodee',[10,20,30]]
print(list1)
print(type(list1))
print(id(list1))

print("list1[0]=",list1[0])
print("list1[0]= Address",id(list1[0]))

print(list1[2])
list1[0]= 120
print(list1)
print(type(list1))
print(id(list1))
print("list1[0]=",list1[0])
print("list1[0]= Address",id(list1[0]))

print('\n++++++++++++++++++++Traversing+++++++++++++++++++++++ ')
print('length: ',len(list1))
print(list1[0])
print(list1[1])

print('\n++++++++++++++++++++slicing list+++++++++++++++++++++++ ')

print(list1[:2])
print(list1[2:])
print(list1[-1:])

print(list1[::2])
print(list1[1::2])

print('\n++++++++++++++++++++combination of traversing and slicing list+++++++++++++++++++++++ ')
l2 = [100,200,300,400,500]
print(l2)
### update the value of index1
l2[1]=50
print(l2)

### update the value of index1 and 2 with new value
l2[1:3]=[600,700]
print(l2)

### replace 400 with empty list
l2[3]=[]
print(l2)

### replace 700,400 with empty list
l2[2:4]=[[],[]]
print(l2)

### delete 700,400 with empty list
l2[2:4]=[]
print(l2)

### delete 600 to the left and add 1000,2000
l2[1:1]=[1000,2000]
print(l2)

print('\n++++++++++++++++++++overloading operators+++++++++++++++++++++++ ')

print(list1+l2)
print(list1*3)

print('\n++++++++++++++Membership operators++++++++++++++++++++ ')
print(list1)
print(120 in list1)
print(12 in l2)
print(10 in list1[-1])

print('\n++++++++++++++Built-in methods++++++++++++++++++++ ')
l3 = ['Math','Comp Sci','English','Algebra']
print(l3)


###Append
l3.append('French')
print(l3)
l3.insert(3,'Calculs')
print(l3)

l3.extend(['Math','Phsycs'])
print(l3)

c1 = l3.pop()
print(l3)
print(c1)

l3.remove('Calculs')
print(l3)


print(l3.count('Math'))
print(l3.index('Math',5))

l3_cp=l3.copy();

l3_cp.sort(reverse=True)
print(l3_cp)

print(l2)
print(sorted(l2))
print(l2)

print(min(l2))
print(max(l2))
print(sum(l2))






























