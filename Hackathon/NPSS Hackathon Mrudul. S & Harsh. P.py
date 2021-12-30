#December 2021, Hackathon, North Park Secondary School
#Number Systems Converter
#By : Mrudul Suresh (735571) , Harsh Patel (678847)


import math as m
flag=True
while flag==True:
    print("\nWelcome to the Number Systems Converter!")
    print("Please type the number option of what you would like to convert:")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Hexadecimal")
    print("4. Hexadecimal to Binary")
    print("5. Decimal to Octal")
    print("6. Octal to Decimal")
    userSelection=int(input())
    
    def decimalToBinary():
        dToBNum=int(input('Please enter your decimal number to convert: '))
        tempList=[]
        finalAnswer=0
        while dToBNum!=0:
            tempList.append (str(dToBNum % 2))
            dToBNum=m.floor(dToBNum/2)
        tempList.reverse()
        print(''.join(tempList))


    def binaryToDecimal():
        bToDNum= input('Please enter your binary number to convert: ')
        decimalNum= int(bToDNum, 2)
        print(decimalNum)
    

    def decimalToHexadecimal():
        dToHNum=int(input('Please enter your decimal number to convert: '))
        conversionList=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        'A' , 'B', 'C', 'D', 'E', 'F']
        hexadecimal=''
        while dToHNum>0:
            remainderNum=(dToHNum%16)
            hexadecimal=conversionList[remainderNum]+hexadecimal
            dToHNum=m.floor(dToHNum/16)
        print(hexadecimal)


    def hexadecimalToDecimal():
        hToDNum=input('Please enter your hexadecimal number to convert: ')
        hToDNum = list(hToDNum)
        toPower=0
        answer=[]
        counter=0
        hToDNum.reverse()

        for i in hToDNum:
            if i=='F':
                i=15
            if i=='E':
                i=14
            if i=='D':
                i=13
            if i=='C':
                i=12
            if i=='B':
                i=11
            if i=='A':
                i=10
            if type(i)==str:
                i=(0+int(i))
            temp2=(16**toPower)
            temp=(temp2*i)
            toPower=toPower+1
            answer.append(temp)
            counter=counter+temp
        print(counter)


    def decimalToOctal():
        na = int(input('Please enter your decimal number to convert: '))
        n = [int(x) for x in str(na)]
        finalans=[]
        div = (na/8)
        nextnum=(m.floor(na/8))
        deci = (div-nextnum)
        finalans.append(deci*8)
        Flag = True
        while Flag == True:
            if (m.floor(div)==0):
                Flag = False
            nextnum2=nextnum
            div=(nextnum/8)
            nextnum=(m.floor(nextnum/8))
            if nextnum==0:
                Flag = False
            deci = (div-nextnum)
            final = (deci*8)
            finalans.append(int(final))
        finalans.reverse()
        for i in finalans:
            print(int(i), end="")
        print("")


    def octalToDecimal():
        na = int(input('Please enter your octal number to convert: '))
        n = [int(x) for x in str(na)]
        toPower=0
        ans=[]
        counter=0
        n.reverse()
        for i in n:
            temp=(8**toPower*i)
            toPower=toPower+1
            counter=counter+temp
            ans.append(temp)
        print(counter)


    if userSelection==1:
        decimalToBinary()
    elif userSelection==2:
        binaryToDecimal()
    elif userSelection==3:
        decimalToHexadecimal()
    elif userSelection==4:
        hexadecimalToDecimal()
    elif userSelection==5:
        decimalToOctal()
    elif userSelection==6:
        octalToDecimal()

    print("\nWould you like to convert another number?")
    print("Please type 'yes' or 'no'.")
    userAgain=input()
    if userAgain=='yes':
        continue
    if userAgain=='no':
        print("Thank you for using our Number Systems Converter program!")
        break

    










        
