def total_calc(bill_amount, tipe_perc):
    total = bill_amount*(1 + 0.01*tipe_perc)
    total = round(total,2)
    print(f"please pay ${total}")
total_calc(150,20)