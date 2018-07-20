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