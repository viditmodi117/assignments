# Write a Python program to get the Fibonacci series of given range.
def fibonacci(n):

    if (n<0):
        print("incorect input")
    elif(n==0):
        return 0
    elif(n==1) or (n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(9))
            