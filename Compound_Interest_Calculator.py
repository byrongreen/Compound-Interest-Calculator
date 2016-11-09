startValue = float(raw_input("What is the present value? "))
Rate = float(raw_input("Interest Rate? (x.x%) ")) / 100
Years = float(raw_input("How many years? "))
endValue = startValue*(1+Rate)**(Years)

print "$" + str(int(endValue))
