# December 2021, Hackathon, North Park Secondary School
# Number Systems Converter
# By : Mrudul Suresh (735571) , Harsh Patel (678847)

import math as m


def choose(userSelection, num):
    if userSelection == 1:
        return decimalToBinary(int(num))
    elif userSelection == 2:
        return binaryToDecimal(str(num))
    elif userSelection == 3:
        return decimalToOctal(int(num))
    elif userSelection == 4:
        return octalToDecimal(int(num))
    elif userSelection == 5:
        return hexadecimalToDecimal(str(num))
    elif userSelection == 6:
        return decimalToHexadecimal(int(num))


def decimalToBinary(dToBNum):
    tempList = []
    finalAnswer = 0
    while dToBNum != 0:
        tempList.append(str(dToBNum % 2))
        dToBNum = m.floor(dToBNum / 2)
    tempList.reverse()
    return ''.join(tempList)


def binaryToDecimal(bToDNum):
    decimalNum = int(bToDNum, 2)
    return decimalNum


def decimalToHexadecimal(dToHNum):
    conversionList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ''
    while dToHNum > 0:
        remainderNum = (dToHNum % 16)
        hexadecimal = conversionList[remainderNum] + hexadecimal
        dToHNum = m.floor(dToHNum / 16)
    return hexadecimal


def hexadecimalToDecimal(hToDNum):
    hToDNum = list(hToDNum)
    toPower = 0
    answer = []
    counter = 0
    hToDNum.reverse()

    for i in hToDNum:
        if i == 'F':
            i = 15
        if i == 'E':
            i = 14
        if i == 'D':
            i = 13
        if i == 'C':
            i = 12
        if i == 'B':
            i = 11
        if i == 'A':
            i = 10
        if type(i) == str:
            i = (0 + int(i))
        temp2 = (16 ** toPower)
        temp = (temp2 * i)
        toPower = toPower + 1
        answer.append(temp)
        counter = counter + temp
    return counter


def decimalToOctal(na):
    n = [int(x) for x in str(na)]
    finalans = []
    div = (na / 8)
    nextnum = (m.floor(na / 8))
    deci = (div - nextnum)
    finalans.append(deci * 8)
    output = []
    Flag = True

    while Flag:
        if m.floor(div) == 0:
            Flag = False
        nextnum2 = nextnum
        div = (nextnum / 8)
        nextnum = (m.floor(nextnum / 8))
        if nextnum == 0:
            Flag = False
        deci = (div - nextnum)
        final = (deci * 8)
        finalans.append(int(final))
    finalans.reverse()
    for i in finalans:
        output.append(str(int(i)))
    return ''.join(output)


def octalToDecimal(na):
    n = [int(x) for x in str(na)]
    toPower = 0
    ans = []
    counter = 0
    n.reverse()
    for i in n:
        temp = (8 ** toPower * i)
        toPower = toPower + 1
        counter = counter + temp
        ans.append(temp)
    return counter
