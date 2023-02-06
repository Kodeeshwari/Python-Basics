'''
    Name - Kodeeshwari
    Question 6 : Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of
s1
'''

str1 = "Kodee"
str2 = "Mimoh"

print("String1",str1,"String2",str2)

lenStr1 = int(len(str1)/2)

firstHalf = str1[:lenStr1]
lastHalf = str1[lenStr1:]

resultStr =  firstHalf + str2 + lastHalf
print(resultStr)

