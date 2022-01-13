stickynotes = []
choice = 'none'

def newstickynote():
    stickynote = input("you jot on a stickynote > ");
    if stickynote == "done":
        return(stickynote)
    else:
        stickynotes.append(stickynote)
        print(stickynote)
        return(stickynote)

def printstickynotes():
    a = 0
    for i in stickynotes:
        print(a,i)
        a += 1

def writestickynotesfile():
    print("## Writing to minddump.txt")
    file = open('minddump.txt', 'w+')
    file.write('\n'.join(stickynotes))
    file.close()

def deleteline():
    print("## Which line to delete?")
    printstickynotes()
    index = int(input("> "))
    print(f"## Deleted {stickynotes[index]}")
    del stickynotes[index]

def userinput():
    userin = input("## Choose an option [new, print, write, delete] > ")
    if userin == "new":
        print("## You selected NEW")
    elif userin == "print":
        print("## You selected PRINT")
    elif userin == "write":
        print("## You selected WRITE")
    elif userin == "delete":
        print("## You selected DELETE")
    elif userin == "goodbye":
        print("## You selected GOODBYE")
    else:
        print("try again")
        return(userinput())
    return(userin)

print("########## GTD Mind Dump #########\n")

while choice != 'goodbye':
    choice = userinput()
    if choice == "new":
        print("## Enter 'done' to exit loop]\n")
        while newstickynote() != 'done':
            1
    elif choice == "print":
        printstickynotes()

    elif choice == "write":
        writestickynotesfile()
    
    elif choice == "delete":
        deleteline()
    
    elif choice == "goodbye":
        print("## Goodbye!")
    
    else:
        print("error")
        exit()
exit()
