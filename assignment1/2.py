'''
    Name - Kodeeshwari
    Question 2 : Accept five int values from user and return their average.
'''

numList = []
sum=0

for i in range(5):
    print("Enter number",i+1)
    num = input()
    numList.append(num)
    sum = sum + int(numList[i])
print(numList)
print("Sum of numbers you entered is",sum)
    
