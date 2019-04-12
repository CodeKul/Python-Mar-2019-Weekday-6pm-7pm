import random

def generateRandomNo():
    no = random.randint(1, 10)
    return no

def inputNo():
    no = int(input("Enter number between 1-10: "))
    return no

def checkForResult(inNo, rnNo):
    if inNo == rnNo:
        print("Won!")
    else:
        print("Better luck next time!\nIt was {}".format(rnNo))

while True:
    inNo = inputNo()
    if inNo == 0:
        print("Bye!")
        break
    elif inNo > 10:
        print("Enter valid number!")
        continue
    rnNo = generateRandomNo()
    checkForResult(inNo, rnNo)
