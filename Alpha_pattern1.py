N=int(input("Enter the no. of rows: "))
for i in range(1,N+1):
    ch=65
    for k in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()