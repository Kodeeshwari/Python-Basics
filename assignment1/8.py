'''
    Name - Kodeeshwari
    Question 8 : Given a two list. Create a third list by picking an odd-index element from the
                 first list and even index elements from second.

'''

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]



print(listOne)
print(listTwo)

oddIndexList = listOne[1::2]
evenIndexList = listTwo[0::2]


###oddIndexList.append(evenIndexList)

###print(oddIndexList)

oddIndexList.extend(evenIndexList)
print(oddIndexList)


