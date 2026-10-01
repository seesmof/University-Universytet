import os

file_name = "process.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, file_name)

with open(file_path, encoding="utf-8", mode="r") as f:
    lines = f.readlines()
answers = 0
for line in lines:
    try:
        question, answer = line.strip().split("? ")
        if answer:
            answers += 1
        print(f"{question} -- {answer}")
    except:
        print(f"! Could not split the question: {line.strip()}")
print(f"\nTotal questions: {len(lines)}")
print(f"Total answered questions: {answers}")
