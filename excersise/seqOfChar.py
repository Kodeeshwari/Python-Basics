'''
    Date 23 Jan 2023
    Author Salar
    Topic Sequence
'''

msg_1 = "I'm a Student!"
msg_2 = 'I\'m a Student!'

print(msg_2)
print(type(msg_2))
print(id(msg_2))

msg_2 = 'I\m a teacher'
print(msg_2)
print(type(msg_2))
print(id(msg_2))

print('\n++++++++++++++ Traverse into sequence +++++++++++')
print(msg_2[0]);print(msg_2[1]);print(msg_2[2])
print(msg_2[-1]);print(msg_2[-2]);print(msg_2[-3])

print('\n++++++++++++++Slice a sequence ++++++++++++++')
print(msg_2[6:13])
s1 = msg_2[6:13]
print(s1)
print(type(s1))
print(id(s1))
s2 = msg_2[:5]
print(s2)
s3 = msg_2[6:]
print(s3)
s4 = msg_2[-7:]
print(s4)

### I'm A student!
s5 = msg_1[:4] + 'A' + msg_1[5:]
print(s5)

print(' hi '*4)

print('\n++++++++++++++++++++++++Built-in methods')
print(len(msg_1))
msg_1_upper=msg_1.upper()
print(msg_1_upper)
msg_1_lower = msg_1.lower()
print(msg_1_lower)

msg = "Introduction to Python"
print(msg)
print(msg.count('py'))
print(msg.count('Py'))
print(msg.count('Python'))
print(msg.count('o'))

print(msg.find('Python'))
print(msg.find('o'))
print(msg.find('o',5))
print(msg.find('o',11))
print(msg.find('o',21))

shopping = 'Fish, Meat, Water, Veg'
myList = shopping.split(', ')
print(myList)

s6='    Hello Guys    '
print(s6)
print(s6.strip())

###input / String Format / F-String





















