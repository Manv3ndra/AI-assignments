def compound_interest(p , r ,t):
    ci = p * pow(1+(r/100) , t) - p
    amt = ci + p
    ci = round(ci ,2)
    amt = round(amt ,2)
    print('Interest =',ci,'Amount =',amt)