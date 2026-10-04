""""
Goal
Practice collecting multiple pieces of information and calculating an average.
Ask the student for:
Student name
Python score
English score
Mathematics score
Calculate the average.
Display a simple result report.
Example
========================================
          STUDENT RESULT
========================================

Student: Ahmed Ali

Python:       85
English:      75
Mathematics:  90
----------------------------------------
Average:      83.33
========================================

Note: Do not create pass/fail conditions yet. Conditions will be covered in Week 2.
Concepts
Input • numbers • arithmetic • formatting

"""

name = input("Student name: ")
python_score = float(input("Python score: "))
english_score = float(input("English score: "))
maths_score = float(input("Mathematics score: "))

average_score = (python_score + english_score + maths_score) / 3
width = 40

print("=" * width)
print("STUDENT RESULTS".center(width))
print("=" * width)
print()
print(f"Student: {name}")
print()
print(f"{'Python:':<16} {python_score:>10.2f}")
print(f"{'English:':<16} {english_score:>10.2f}")
print(f"{'Maths:':<16} {maths_score:>10.2f}")
print("-" * width)
print(f"{'Average:'}{average_score:>10.2f}")
print("=" * width)

