P=eval(input("Enter the principal amount: "))
R=eval(input("Enter the rate: "))
T=eval(input("Enter the time period: "))
CI=P*((1+R/100)**T)-P
TA=P+CI
print("Compound interest is: ", CI, "\n","Total amount is:, ", TA)