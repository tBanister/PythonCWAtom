nums = []
counter = 0
newnum = 0
total = 0
sum = 1
amount = int(input("How many inputs?"))

while counter < amount:
    newnum = int(input("new number"))
    nums.append(newnum)
    total += newnum
    sum *= newnum
    counter += 1


done = False
while done == False:
    AorM = input("'a' for Addition or 'm' for Multiply")
    if AorM.lower() == "a":
        print("Addition =",total)
        done = True
    elif AorM.lower() == "m":
        print("Multiply =", sum)
        done = True
    else:
        print("'a' or 'm' only")



    



