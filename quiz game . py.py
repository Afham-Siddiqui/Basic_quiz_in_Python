print("QUIZ GAME.")
print("Hello, Welcome to this game!")
ans = input("Are you ready to play this game (yes/no):")
score = 0
total_Q = 5

if ans.lower() == "yes":
    ans = input("1,which team is the winner of 2019 Cricket World Cup? ")
    if ans.lower() == "england":
        score += 1
        print("correct")
    else:
        print("incorrect")

    ans = input("2,which is the runner-up team in 2019 Cricket World Cup? ")
    if ans.lower() == "new zealand":
        score += 1
        print("correct")
    else:
        print("incorrect")

    ans = input("3,what is the data type of alphabetic data? ")
    if ans.lower() == "string":
        score += 1
        print("correct")
    else:
        print("incorrect")

    ans = input("4,what is the data type of numeric data? ")
    if ans.lower() == "integer":
        score += 1
        print("correct")
    else:
        print("incorrect")

    ans = input("5,what is the full form of AI? ")
    if ans.lower() == "artificial intelligence":
        score += 1
        print("correct")
    else:
        print("incorrect")


print("Thank you for playing this game you got", score , "question correct.")
mark = (score/total_Q) * 100
print("mark: ", str(mark))
print("Good Bye")