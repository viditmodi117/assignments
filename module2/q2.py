# Write a Python program to get the Factorial number of given number.
num = int(input("Enter a num:"))
factorial = 1
if(num<0):
    print("factorial does not exist for negative number")
elif(num==0):
    print("factorial 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of",num,"is",factorial)            