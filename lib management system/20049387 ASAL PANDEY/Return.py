import Split
import DateTime
def returnBook():
    name=input("Enter name of borrower: ")
    a="Borrow-"+name+".txt"
    try:
        
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        returnBook()

    b="Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("               college Library Management System \n")
        f.write("                   Returned By: "+ name+"\n")
        f.write("    Date: " + DateTime.getDate()+"    Time:"+ DateTime.getTime()+"\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")


    total=0.0
    for i in range(3):
        if Split.bookname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+Split.bookname[i]+"\t\t$"+Split.cost[i]+"\n")
                Split.quantity[i]=int(Split.quantity[i])+1
            total+=float(Split.cost[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=1.5*day
        
        with open(b,"a")as f:
            f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    


    print("Final Total: "+ "$"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: $"+ str(total))
    
        
    with open("Books.txt","w+") as f:
            for i in range(3):
                f.write(Split.bookname[i]+","+Split.authorname[i]+","+str(Split.quantity[i])+","+"$"+Split.cost[i]+"\n")
