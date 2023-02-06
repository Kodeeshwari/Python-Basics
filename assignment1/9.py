'''
    Name - Kodeeshwari
    Question 9 : Given an input list removes the element at index 4 and add it to the 2nd
                 position and also, at the end of the list

'''

List = [54, 44, 27, 79, 91, 41]


print("The given list:",List)

removedElement = List.pop(4)
print("Removed 4th index value",List)

List[2]=removedElement
print("Added removed element to 2nd position",List)

List.append(removedElement)
print("Appended removed element to the list",List)


