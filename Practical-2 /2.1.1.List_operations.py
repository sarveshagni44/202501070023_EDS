# Write a Python program that implements a menu-driven interface for managing a list of integers. The program should have the following menu options:
1. Add
2. Remove
3. Display
4. Quit

# code :

List = []   # Creating list outside loop

while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")

	n = int(input("Enter choice: "))

	if n == 1:
		integer = int(input("Integer: "))
		List.append(integer)
		print("List after adding:", List)

	elif n == 2:
		if len(List) == 0:
			print("List is empty")
		else:
			val = int(input("Integer: "))
			if val in List:
				List.remove(val)
				print("List after removing:", List)
			else:
				print("Element not found")

	elif n == 3:
		if len(List) != 0:
			print(List)
		else:
			print("List is empty")

	elif n == 4:
		print()
		break

	else:
		print("Invalid choice")
