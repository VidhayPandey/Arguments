def total_calc(bill,tip):
    total=bill*(1+0.01*tip)
    total= round(total,2)
    print(f"Please pay ${total}")


amount=int(input("Please Enter Bill Amount: "))
tip=int(input("Please Enter the Tip Percentage: "))
total_calc(amount,tip)