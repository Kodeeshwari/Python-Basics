'''
    Name - Kodeeshwari
    Question 1 : Accept two int values from user and return their product. If the product is
                 greater than 1000, then return their sum
'''
print("Enter number1")
num1 = input()

print("Enter number2")
num2 = input()

result = int(num1)*int(num2)

print("The product of",num1,"and",num2, "is",result)

if result>1000:
    print("The sum of",num1,"and",num2, "is",int(num1)+int(num2))

