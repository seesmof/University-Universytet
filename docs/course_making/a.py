import os


folders = [
    "exams",
    "notes",
    "stuff",
    "tasks",
    "terms",
]
course_name = input("Введіть назву курсу: ")
course_name = course_name.upper().strip()

current_dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(current_dir, "..", "..")

course_dir = os.path.join(root, course_name)
os.mkdir(course_dir)
for folder in folders:
    os.mkdir(os.path.join(course_dir, folder))
