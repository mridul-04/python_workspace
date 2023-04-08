for i in range(5):
    cp=int(input("enter your cost price : "))
    sp=int(input("enter your selling price : "))
    if cp < sp:
        profit = (sp-cp)
        profit_percent=(profit/cp*100)
        print("profit of : ", profit)
        print("profit percent = ",profit/cp*100)
    elif sp<cp:
        loss=(cp-sp)
        loss_percent=(loss/cp*100)
        print("loss of : ", loss)
        print("loss percent = ",loss/cp*100)



