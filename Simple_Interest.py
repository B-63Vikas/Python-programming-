P=eval(input("Enter the principal amount: "))
R=eval(input("Enter the rate: "))
T=eval(input("Enter the time period: "))
S_I=(P*R*T)/100
T_A=P+S_I
print("Simple Interest: ", S_I,"\n","Total Amount: ", T_A)