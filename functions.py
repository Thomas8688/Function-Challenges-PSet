from random import randint


def randomChallenge():
    challengeList = []
    with open("FunctionChallenges.txt", "r") as myFile:
        challenges = myFile.readlines()
        for challenge in challenges:
            if challenge != "\n":
                challengeList.append(challenge)
    index = randint(0,len(challengeList))
    print(challengeList[index])


def maxNum():
    listOfNums = []
    for i in range(3):
        valid = False
        while not valid:
            newNum = input("number: ")
            try:
                int(newNum)
                valid = True
            except:
                print("invalid input")
    highest = listOfNums[0]
    for i in range(1,3):
        if listOfNums[i] > highest:
            highest = listOfNums[i]
    print("highest: ", highest)


def add(numList):
    if isinstance(numList, list):
        ints = True
        for i in range(len(numList)):
            try:
                int(numList[i])
                numList[i] = int(numList[i])
            except:
                ints = False
        if ints:
            sum = 0
            for num in numList:
                sum += num
            print("sum:",sum)
        else:
            print("numList must be a list of numbers")
    else:
        print("numList must be a list of numbers")


def mult(numList):
    if isinstance(numList, list):
        ints = True
        for i in range(len(numList)):
            try:
                int(numList[i])
                numList[i] = int(numList[i])
            except:
                ints = False
    else:
        print("numList must be a list of numbers")
    if ints:
        sum = 1
        for num in numList:
            sum *= num
        print(sum)
    else:
        print("numList must be a list of numbers")



def rev(anyList):
    #print(anyList[::-1]) if isinstance(anyList, list) else print("anyList must be a list")
    if isinstance(anyList, list):
        print(anyList[::-1])
    else:
        print("anylist must be a list")


def factFunc(num):
    if isinstance(num, int) and num > 0:
        if num == 1:
            return 1
        else:
            return num * factFunc(num-1)
    else:
        print("num must be an integer")

def fact(num):
    print(factFunc(num))


def inRange(num, rangeList):
    if isinstance(rangeList, list) and len(rangeList) == 2:
        rangeInt = True
        for i in range(len(rangeList)):
            try:
                int(rangeList[i])
                rangeList[i] = int(rangeList[i])
            except:
                rangeInt = False
        numInt = True
        try:
            int(num)
            num = int(num)
        except:
            numInt = False
    if rangeInt and numInt:
        rangeList = sorted(rangeList)
        if num >= rangeList[0] and num <= rangeList[1]:
            print("true")
        else:
            print("false")
    else:
        print("num must be a number and rangeList must contain two numbers only")

def cases(string):
    if isinstance(string, str):
        uppers = 0
        lowers = 0
        string = list(string)
        for letter in string:
            if ord(letter.lower()) > 96 and ord(letter.lower()) <  123:
                if letter == letter.upper():
                    uppers += 1
                else:
                    lowers += 1
        print("lower:", lowers)
        print("upper:", uppers)
    else:
        print("string must be a string")

def unique(charList):
    if isinstance(charList, list):
        returner = []
        for item in charList:
            if item not in returner:
                returner.append(item)
        print(returner)
    else:
        print("charList must be a list")

def prime(number):
    if isinstance(number, int) and number > 0:
        prime = "true"
        for i in range(2, number):
            if (number % i == 0):
                prime = "false"
        if number == 1:
            print("false")
        else:
            print(prime)
    else:
        print("number must be an integer above 0")

def evens(numList):
    if isinstance(numList, list):
        nums = True
        for i in range(len(numList)):
            try:
                int(numList[i])
                numList[i] = int(numList[i])
            except:
                nums = False
        if nums:
            evens = []
            for item in numList:
                if item % 2 == 0:
                    evens.append(item)
            print(evens)
        else:
            print("all items in numList must be integers")
    else:
        print("numList must be a list of integers")
