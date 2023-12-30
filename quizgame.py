print("Welcome to the video game quiz!") ##welcome message

play = input("Would you like to start the game? ")

if play.lower() !="yes":
            quit()

print("Let's GO!")

Points = 0 #point counter
answer = input("What is the name of the main character from Santa Monca's God of War series? ")

if answer.lower() == "kratos":
    print("correct!")
    Points += 1
    print("current points: " + str(Points)) #point counter
else:
    print("incorrect")

answer = input("What game did Naked Snake lose his eye? ")

if answer.lower() == "metal gear solid 3":
    print("correct!")
    Points += 1
    print("current points: " + str(Points)) #point counter
else:
    print("incorrect")

answer = input("What title is Geralt of Rivia the protagonist of? ")

if answer.lower() == "the witcher":
    print("correct!")
    Points += 1
    print("current points: " + str(Points)) #point counter
else:
    print("incorrect")
print("you're done!")
print("Your answer rate is: " + str((Points/ 3) * 100 ) + "%") #final correct answer rate which is a string of the current point converted into percentage rate
