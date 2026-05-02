import math
N=int(input())

if(0<N<10):
	print(N**2)

elif(10<=N<=99):
	result=math.sqrt(N)
	print(f"{result:.2f}")

elif(100<=N<=999):
	result=N**(1/3)
	print(f"{result:.2f}")

else:
	print("Invalid")
