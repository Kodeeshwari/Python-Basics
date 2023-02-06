'''
    Name - Kodeeshwari
    Question 5 :  Given a list of ints, return True if first and last number of a list is same
'''

numList = [10,20,30,40,10]
listLen = len(numList)

print(numList)
isSame = False
if numList[0]==numList[listLen-1]:
    isSame = True;
    print("first and last elements in list is same",isSame)
else:
    isSame = False;
    print("first and last elements in list is not same",isSame)
