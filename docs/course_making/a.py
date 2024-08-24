import os


def create_folder(course_name: str):
    course_dir = os.path.join(root, course_name)
    os.mkdir(course_dir)


current_dir = os.path.dirname(os.path.abspath(__file__))
courses = os.path.join(current_dir, "..", "courses")
root = os.path.join(current_dir, "..", "..")
current_id = "31"

with open(os.path.join(courses, current_id + ".txt"), "r", encoding="utf-8") as f:
    courses = f.read().splitlines()
for course in courses:
    create_folder(course)
