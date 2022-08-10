totcakeqty=int(input("enter the quantity"))
totbreadqty=int(input("enter the quantity"))
cakecp=20
cakesp=40
breadcp=10
breadsp=15
customer=0
emp=int(input("enter employees"))

empsal=emp*100
cake=0
bread=0
totsp=0
totcp=1
profit=0
loss=0
totcp=(totcakeqty*cakecp)+(totbreadqty*breadcp)
for i in range(1,10):   
    if(totcakeqty>0 and totbreadqty >0):
        customer=int(input("enter customer"))
        cake=int(input("enter cakes you want"))
        bread=int(input("enter breads you want"))          
        totsp=totsp+cake*cakesp +bread*breadsp
        totcakeqty=totcakeqty-cake
        totbreadqty=totbreadqty-bread
    else:
        print("not available")
        break
totsp=totsp-empsal
print(totsp)
print(totcp)
profit=totsp-totcp
loss=totcp-totsp
if(profit>loss):
    print("profit")
    print(profit)
else:
    print("loss")
    print(loss)
    
    