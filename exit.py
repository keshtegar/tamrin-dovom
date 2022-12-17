#exit
a=[]
x=1
while x==1:
    n=int(input("please enter a number: "))
    a.append(n)
    
    i=input(" را بزنیدy  را یزنید در غیر اینص.رت exit  اگر میخواهید خارج ش.ید ")
    if i=="exit":
        break
    elif i=="y":
        x=1
sum1=sum(a)
print("sum = ",sum1)


    
