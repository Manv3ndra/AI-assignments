import compount_interest as ci

principal = input('Enter the principal amount: ')
rate = input('Enter the rate of interest: ')
time = input('Enter the time: ')
ci.compound_interest(float(principal) , float(rate) , int(time))