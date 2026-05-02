#Write a Python program that takes an integer as input and prints the multiplication table for that integer from 1 to 10.
#code

num=int(input())

for i in range(1,11):
	print(num,"x",i,"=",num*i)
