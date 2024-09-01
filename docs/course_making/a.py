import os


def create_folder(course_name: str):
    course_dir = os.path.join(root, course_name)
    os.mkdir(course_dir)

    for nested_folder in nested_folders:
        os.mkdir(os.path.join(course_dir, nested_folder))


current_dir = os.path.dirname(os.path.abspath(__file__))
courses = os.path.join(current_dir, "..", "courses")
root = os.path.join(current_dir, "..", "..")
current_id = "31"
nested_folders = ["file", "task"]

with open(os.path.join(courses, current_id + ".txt"), "r", encoding="utf-8") as f:
    courses = f.read().splitlines()
for course in courses:
    create_folder(course)
