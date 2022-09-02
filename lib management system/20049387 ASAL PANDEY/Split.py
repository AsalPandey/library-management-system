def listSplit():
    global bookname
    global authorname
    global quantity
    global cost
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    with open("Books.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            count=0
            for a in lines[i].split(','):
                if(count==0):
                    bookname.append(a)
                elif(count==1):
                    authorname.append(a)
                elif(count==2):
                    quantity.append(a)
                elif(count==3):
                    cost.append(a.strip("$"))
                count=count+1
