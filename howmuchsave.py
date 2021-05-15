
print ("How much should you save?")
currency = input ("Enter currency: ")
age = int(input ("How old are you? "))
old = int(input ("Up to what age do you expect to live? "))
ext_savings = int(input (f"How much have you invested already (in {currency.upper()})? "))
money = int(input (f"How much money would you need every month if you retired today (in {currency.upper()})? " ))
inflation = 2
growth = 7
dividend = 2
ret_fund = 0

# HALLO ANDY
def calculation (currency, age, old, ext_savings, inflation, growth, money, ret_fund):
    retire = int (input ("What age would you like to be financially independent? "))
    retire1 = retire
    funds = int(0)
    monthly = int(0)
    stocks = int(ext_savings*(1-(age/100)))
    bonds = int(ext_savings*(age/100))
    money = (money*12)*((inflation/100 + 1)**(retire-age))
    money2 = money
    ### Calculate money needed during retirement in nominal value
    while retire1 <= old:
        ret_fund += money
        money = money*(inflation/100 + 1)
        retire1 +=1
        
    ### Calculate money needed to reach that amount during working life, considering stock & bond growth
    while True:
        age2 = age
        stocks2 = stocks
        bonds2 = bonds
        retire2 = retire
        money3 = money2
        dividend_pay = 0
        while age < retire:
            ### growth+pay-in+dividend reinvestment
            stocks = stocks*(1+(growth/100))+((monthly*12)*(1-(age/100)))+stocks*(dividend/100)
            bonds = bonds*(1+(inflation/100))+((monthly*12)*(age/100))+bonds*(inflation/100)
            age += 1
            print ("pre-retirement funds:", int(stocks+bonds), "age:", age)
        while retire <= old:
            stocks = stocks*(1+(growth/100))-((money-(stocks*(dividend/100)+bonds*(inflation/100)))*(retire/100))
            bonds = bonds*(1+(inflation/100))-((money-(stocks*(dividend/100)+bonds*(inflation/100)))*(1-retire/100))
            dividend_pay = stocks*(dividend/100)+bonds*(inflation/100)
            funds = stocks + bonds 
            money = money*(inflation/100 + 1)
            retire += 1
            print ("post-retirement funds: ", int(funds), "age:", retire)
            print ("annual expense: ", int(money))
            print ("stock growth amount: ", int(stocks*(growth/100)))
            print ("stocks: ", int(stocks))
            print ("bonds: ", int(bonds))
            print ("dividend earned: ", int(dividend_pay))
            print ("consuming bonds")
            if retire==old and funds > money:
                        print ("Funds left at death: ", int(funds), f"{currency.upper()}")
                        print ("Yearly living expenses at death: ", int(money), f"{currency.upper()}")
                        print ("\n" f"Assumption:" "\n" f"{inflation}% inflation" "\n" f"{growth}% annual stock index growth" "\n" f"{inflation}% return on govt. bonds" "\n" "Portfolio bond share proportional to age (e.g. 50 years old, 50% bonds)""\n")
                        print (f"You need to invest {monthly} {currency.upper()} monthly" "\n")
                        return 1 
            ### changed money consumption pattern, too much money needed now

            if bonds <= 0 :
                while retire <= old:
                    stocks = stocks*(1+(growth/100))-(money+(stocks*(dividend/100)))
                    dividend_pay = stocks*(dividend/100)
                    funds = stocks 
                    money = money*(inflation/100 + 1)
                    retire += 1
                    print ("post-retirement funds: ", int(funds), "age:", retire)
                    print ("annual expense: ", int(money))
                    print ("stock growth amount: ", int(stocks*(growth/100)))
                    print ("dividend earned: ", int(dividend_pay))
                    print ("out of bonds, consuming stock")
                    if retire==old and funds > money:
                        print ("Funds left at death: ", int(funds), f"{currency.upper()}")
                        print ("Yearly living expenses at death: ", int(money), f"{currency.upper()}")
                        print ("\n" f"Assumption:" "\n" f"{inflation}% inflation" "\n" f"{growth}% annual stock index growth" "\n" f"{inflation}% return on govt. bonds" "\n" "Portfolio bond share proportional to age (e.g. 50 years old, 50% bonds)""\n")
                        print (f"You need to invest {monthly} {currency.upper()} monthly" "\n")
                        return 1 
        age = age2
        stocks = stocks2
        bonds = bonds2
        retire = retire2
        money = money3
        dividend_pay = 0 
        monthly += 50
  
    
    ###+((monthly*12)*(1-(age/100))),((monthly*12)*(age/100)),monthly = "{:,}".format(int(monthly))


            



def continuation():
    continuation_input = int(input ("Try a different age? (1 = Yes/2 = No)? "))
    if continuation_input == 1:
        calculation (currency, age, old, ext_savings, inflation, growth, money, ret_fund)
        continuation()
    else:
        print ("Bye")

calculation (currency, age, old, ext_savings, inflation, growth, money, ret_fund)
continuation()