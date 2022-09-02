import DateTime
import Split

def borrowBook():
    success=False
    while(True):
        firstName=input("Enter the first name of the borrower: ")
        if firstName.isalpha():
            break
        print("please input a valid name")
    while(True):
        lastName=input("Enter the last name of the borrower: ")
        if lastName.isalpha():
            break
        print("please input a valid name")
            
    t="Borrow-"+firstName+".txt"
    with open(t,"w+") as f:
        f.write("              college Library Management System  \n")
        f.write("                   Borrowed By: "+ firstName+" "+lastName+"\n")
        f.write("    Date: " + DateTime.getDate()+"    Time:"+ DateTime.getTime()+"\n\n")
        f.write("S.N. \t Bookname \t Authorname  \t  quantity  \t cost \n")
    
    while success==False:
        print("Please select a option below:")
        for i in range(len(Split.bookname)):
            print("Enter", i, "to borrow book", Split.bookname[i])
    
        try:   
            a=int(input())
            try:
                if(int(Split.quantity[a])>0):
                    print("Book is available")
                    with open(t,"a") as f:
                        f.write("1. \t"+ Split.bookname[a]+"\t  "+Split.authorname[a]+" \t "+Split.quantity[a]+" \t\t "+Split.cost[a]+"\n")

                    Split.quantity[a]=int(Split.quantity[a])-1
                    with open("Books.txt","w+") as f:
                        for i in range(3):
                            f.write(Split.bookname[i]+","+Split.authorname[i]+","+str(Split.quantity[i])+","+"$"+Split.cost[i]+"\n")


                    #code for borrowing more than one book.
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow more books?. Press y for yes and n for no.(note:you cannot borrow the same book twice)"))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(Split.bookname)):
                                print("Enter", i, "to borrow book", Split.bookname[i])
                            a=int(input())
                            if(int(Split.quantity[a])>0):
                                print("Book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t"+ Split.bookname[a]+"\t "+Split.authorname[a]+"\t "+Split.quantity[a]+" \t\t "+Split.cost[a]+"\n")

                                Split.quantity[a]=int(Split.quantity[a])-1
                                with open("Books.txt","w+") as f:
                                    for i in range(3):
                                        f.write(Split.bookname[i]+","+Split.authorname[i]+","+str(Split.quantity[i])+","+"$"+Split.cost[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books from us. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Book is not available now!")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose book acording to their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")
