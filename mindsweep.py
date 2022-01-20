stickynotes = []
f = ['\nFamily'] # family
w = ['\nWork'] # work
h = ['\nHouse'] # house

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

def sortstickynotes():
    print(f"Sorting {len(stickynotes)} sticky notes. Input (f)amily, (w)ork, (h)ouse for each")
    for i in stickynotes:
        print(i)
        category = input("[f,w,h]> ")
        if category == 'f':
            a = i
            f.append(a)
            #stickynotes.remove(a)
        elif category == 'w':
            a = i
            w.append(a)
            #stickynotes.remove(a)
        elif category == 'h':
            a = i
            h.append(a)
            #stickynotes.remove(a)
        else:
            sortstickynotes()
    print("Family")
    print(f)
    print("Work")
    print(w)
    print("House")
    print(h)
    file = open('mindsweepsorted.txt', 'w+')
    file.write('\nSorted List')
    file.close()
    file = open('mindsweepsorted.txt', 'a+')
    file.write('\n'.join(f))
    file.write('\n'.join(w))
    file.write('\n'.join(h))
    file.close()

def writestickynotesfile():
    print("## Writing to mindsweep.txt")
    file = open('mindsweep.txt', 'w+')
    file.write('\n'.join(stickynotes))
    file.close()

def deleteline():
    print("## Which line to delete?")
    printstickynotes()
    index = int(input("> "))
    print(f"## Deleted {stickynotes[index]}")
    del stickynotes[index]

def userinput():
    userin = input("## Choose an option [new, print, write, delete, sort] > ")
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
    elif userin == "sort":
        print("## You Selected SORT")
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

    elif choice == "sort":
        sortstickynotes()
    
    elif choice == "goodbye":
        print("## Goodbye!")
    
    else:
        print("error")
        exit()
exit()
