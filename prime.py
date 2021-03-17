n = int(input("Enter the number: "))
for i in range(2,n):
    if n%i==0:
	print("prime no.")
	break
else:
    print("Not a prime")