#program to find whether the number is armstrong//
N=int(input("Enter the number: "))
sum=0
Temp=N
while N!=0:
    Digit = N % 10
    sum+=Digit**3
    N=N//10
if sum==Temp:
    print("The number is armstrong number")
else:
    print("The number is not an armstrong number")