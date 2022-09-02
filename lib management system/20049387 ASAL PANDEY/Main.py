import Return
import Split
import DateTime
import Borrow

def start():
    while(True):
        print("        Welcome to our college library management system     ")
        print("------------------------------------------------------")
        print("input 1. To Display the books")
        print("input 2. To Borrow a book")
        print("input 3. To return a book")
        print("input 4. To exit")
        try:
            choose=int(input("Select a choice from 1-4: "))
            print()
            if(choose==1):
                with open("Books.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(choose==2):
                Split.listSplit()
                Borrow.borrowBook()
            elif(choose==3):
                Split.listSplit()
                Return.returnBook()
            elif(choose==4):
                print("Thank you for using college library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please enter a valid choice from 1-4")
start()
