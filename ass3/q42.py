# Write a Python function that checks whether a passed string is palindrome or not 

# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "wow"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
