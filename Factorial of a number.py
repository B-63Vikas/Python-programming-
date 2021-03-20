N=eval(input("ENTER THE NUMBER: "))
Fact=1
i=1
if N<0:
    print("Factorial doesn't exist")
elif N==0:
    print("Factorial of zero is 0")
else:
    for i in range(1,N+1):
         Fact = Fact*i
    print("Factorial of", N, "is", Fact)




