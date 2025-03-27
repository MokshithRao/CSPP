def Home_loan(a,ai,cs,cd):
    if (25<=a<=65 and ai>=50000 and cs>=700 and cd<50000) or (a<25 and ai>=75000 and cs>=750 and cd<30000) or (a>65 and ai>=40000 and cs>=650 and cd<20000):
        return True
    else:
        return False
print(Home_loan(int(input()), float(input()), int(input()), float(input())))
