Amount=eval(input("Enter the amount: "))
print("No. of 2000 notes: ", int((Amount)/2000))
print("No. of 500 notes: ", int((Amount%2000)/500))
print("No. of 100 notes: ", int(((Amount%2000)%500)/100))