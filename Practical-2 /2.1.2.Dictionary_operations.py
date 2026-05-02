# Write a Python program to perform insertion, update, deletion, and traversal operations on a dictionary. An initial dictionary containing 10 predefined records is already given in the program.
# code :

# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# Display original dictionary
print("Original Dictionary:", student)

# Insertion
key = int(input())
value = input()
student[key] = value
print("After Insertion:", student)

# Update
update_key = int(input())
update_value = input()

if update_key in student:
	student.update({update_key: update_value})

print("After Update:", student)

# Deletion
delete_key = int(input())

if delete_key in student:
	student.pop(delete_key)

print("After Deletion:", student)

# Traversal
print("Traversing Dictionary:")
for k, v in student.items():
	print(k, ":", v)
