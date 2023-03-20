import random as rm

dictionary = open("Dict.txt")
answers=open("Answers.txt")

y = rm.randint(0,2322)
for x in range(y):
    answers.readline()
answer = answers.readline()

def printBoxes(inp):
    for x in range(5):
        if inp[x] == answer[x]:
            print('\033[92m',f' {inp[x]} ','\033[0m',end='')
        elif inp[x] in answer:
            print('\033[96m',f' {inp[x]} ','\033[0m',end='')
        else:
            print('\033[95m',f' {inp[x]} ','\033[0m',end='')
    print("")


print("Let's Play Wordle")
printBoxes("      ")
for x in range(6):
    dictionary = open("Dict.txt")
    inp=input("Enter a Word:")
    if len(inp)==5 and (inp+"\n") in dictionary:
        printBoxes(inp.upper())
        print(answer)
    else:
        print("invalid input")
print("Answer was ",answer)