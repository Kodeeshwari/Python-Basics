'''
    Name - Kodeeshwari
    Question 4 : Given a string and an int n, remove characters from string starting from zero
                   upto n and return a new string
'''

str = input("Enter String\n")
num = input("Enter number to remove characters from string from Zero to number\n")

removeChars = str.replace(str[:int(num)], '')
print(removeChars)

    
