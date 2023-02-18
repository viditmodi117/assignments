# Write a Python program to check a list is empty or not.

def Enquiry(lis1):
	if not lis1:
		return 1
	else:
		return 0

# Driver Code
lis1 = []
if Enquiry(lis1):
	print("The list is Empty")
else:
	print("The list is not empty")
