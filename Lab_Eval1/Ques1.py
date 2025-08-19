# Dictionary of student marks
marks = {"Alice": 82, "Bob": 60, "Charlie": 91, "David": 45, "Eva": 76}

# Find students scoring more than 75
high_scorers = [name for name, score in marks.items() if score > 75]

if high_scorers:
    print("Students scoring more than 75:")
    for student in high_scorers:
        print(student)
else:
    print("No high scorer found.")
