#Write a pyton program to determine the grades of the students based on their aggregate percentage.
#code

n = int(input())
marks = list(map(int, input().split()))
fail=False
# Check fail condition
for m in marks:
	if m < 40:
		fail=True
		break
if fail:
	print("Fail")
# If passe
else:
	total = sum(marks)
	percentage = total / n

	print(f"Aggregate Percentage: {percentage:.2f}")

	if percentage >= 75:
		print("Grade: Distinction")
	elif percentage >= 60:
		print("Grade: First Division")
	elif percentage >= 50:
		print("Grade: Second Division")
	else:
		print("Grade: Third Division")
