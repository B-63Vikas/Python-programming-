N=int(input("Enter no. of rows: "))
ch=65
for i in range(1,N+1):
    for k in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()