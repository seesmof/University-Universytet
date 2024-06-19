import os

current_dir: str = os.path.dirname(os.path.abspath(__file__))
gitignore_path: str = os.path.join(current_dir, ".gitignore")
large_files: list[str] = []

for root, dirs, files in os.walk(current_dir):
    for file in files:
        file_size: int = os.path.getsize(os.path.join(root, file))
        size_limit: int = 100 * 1024 * 1024

        if file_size >= size_limit:
            file_path: str = os.path.join(root, file)
            large_files.append(file_path)

with open(gitignore_path, "w", encoding="utf-8") as gitignore:
    for file in large_files:
        gitignore.write(f"{file}\n")
