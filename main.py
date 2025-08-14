userName = ["Carl","Tasmin","Eric","Zoe","Alan","Mark"]
print("List of unsorted names: ",userName)
numItems = len(userName)
while numItems > 1:
    for count in range(numItems - 1):
        swapped = False
        if userName[count] > userName[count+1]:
            swapped = True
            temp = userName[count]
            userName[count] = userName[count+1]
            userName[count+1] = temp
    numItems = numItems - 1
print(userName)