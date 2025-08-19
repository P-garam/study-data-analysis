# 1. Calculate average from a list and use conditional statements
scores = [95, 70, 88, 100, 67]
print(sum(scores))
average = sum(scores) / len(scores)

if average >= 80:
    print("Average score is", average, "→ Pass")
else:
    print("Average score is", average, "→ Fail")


# 2. Dictionary practice (Python's key-value structure)
student = {
    "name": "Garam",
    "major": "Data Science",
    "age": 21
}

print("\nStudent Info:")
print("Name:", student["name"])
print("Major:", student["major"])
print("Age:", student["age"])


# 3. Loop through list and apply condition
print("\nScores above 90:")
for score in scores:
    if score >= 90:
        print(score)


# 4. Get user input and use if/elif/else to classify score
user_score = int(input("\nEnter your score: "))

if user_score >= 90:
    print("Your grade is A")
elif user_score >= 80:
    print("Your grade is B")
else:
    print("Your grade is C or below")
