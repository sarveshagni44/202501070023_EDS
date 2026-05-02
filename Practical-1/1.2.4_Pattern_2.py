#Write a Python program to print a right-angled triangle pattern of numbers.
# code :

n=int(input())
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=" ")
	print()
