''' BubbleSort
'''

# A List for the DEMO
def PrintList(TheList):
    a = 0
    while a < len(TheList):
        print("Element #", a,
            "is", TheList[a]);
        a += 1
    
print("Bubble, Bubble...");

NamesList = [
     "Pat", "Bill", "Larry", "Lily", "Jane",
     "Millie", "Ichiro", "Bob"
]
PrintList(NamesList)

# The SORT Routine
InOrder = False
while(not InOrder):
        InOrder = True
        n = 0
        while n < len(NamesList) - 1:
            if NamesList[n] > NamesList[n+1]:
                InOrder = False
                temp = NamesList[n]
                NamesList[n] = NamesList[n+1]
                NamesList[n+1] = temp
            n += 1

print("\n ...Toil & Trouble")
PrintList(NamesList)

# Using Python's Special Assignment
InOrder = False
while(not InOrder):
        InOrder = True
        n = 0
        while n < len(NamesList) - 1:
            if NamesList[n] > NamesList[n+1]:
                InOrder = False
                NamesList[n], NamesList[n+1] = \
                      NamesList[n+1], NamesList[n]
            n += 1

print("\n Python's Special Assignment")
PrintList(NamesList)
