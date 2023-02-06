'''
    Name - Kodeeshwari
    Question 3 : Given a string of odd length greater 7, return a string made of the middle three
                 chars of a given String.
'''

str = input("Enter Odd String length more than 7\n")
strLength = len(str)


if (strLength % 2 == 1) & (strLength > 7):
    midStrPos = int(strLength/2)
    print(str[midStrPos:midStrPos+3])
else :
    print("Please make sure string length is odd number and more than 7")
    
