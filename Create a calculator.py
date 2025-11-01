costOfBill = float(input("Enter how much was the bill: "))

def caculateBill():
    howMuchTip = float(input("Enter how much to tip(in a decimal): "))
    totalCost = costOfBill + (costOfBill*howMuchTip)
    return print(totalCost)
caculateBill()
