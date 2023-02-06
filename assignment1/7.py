'''
    Name - Kodeeshwari
    Question 7 : Find all occurrences of “USA” in given string (uppercase and lowercase).
s1

'''

str = "Welcome to USA. usa awesome, isn't it?"


print(str)
strToLower = str.lower()
###print("USA".lower())
resultStr = strToLower.count("USA".lower())
print("usa occurs",resultStr,"times")

