
#exersice1
for number in range(0,101):
 print (number)
 # extra credit#
previousNumber=0
for number in range(1, 101):
    previousNumber= previousNumber+number
    print(previousNumber)


#exersice2
useInput = input("Enter a number: ")
print("1")


#exersice3
while True:
    useInput = input("Enter a number or 'q' to quit")
    if useInput == "q":
        break

#exersice4
while True:
    useInput = input("Enter a number")
    if useInput == useInput:
        break

#exersice5
def forLoopFunction():

    smallArray=[]
    while True:
     userInput=input("whatever?: or 'q' to quit  ")
     if userInput== "q":
         for a in smallArray:
            print(a)
         break
     else:smallArray.append(userInput)

forLoopFunction()
