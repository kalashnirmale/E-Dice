import random
print("Virtual DICE")       
dice = "m"                                 
while dice == "m":                         
    number = random.randint(1,6) #will print any random number from 1-6      
    if number == 1:
        print("-----1-----")
    if number == 2:
        print("-----2-----")
    if number == 3:
       print("-----3-----")
    if number == 4:
        print("-----4-----")
    if number == 5:
        print("-----5-----")
    if number == 6:
        print("-----6-----")
    dice = input("press m to Role\n")      
