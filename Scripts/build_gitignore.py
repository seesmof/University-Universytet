import os
from rich.console import Console
from rich.traceback import install

install()
console = Console()

from constants import Constants as c

gitignore_path: str = os.path.join(c.ROOT_DIR, ".gitignore")
large_files: list[str] = [
    "__pycache__",
]

for root, dirs, files in os.walk(c.ROOT_DIR):
    for file in files:
        file_size: int = os.path.getsize(os.path.join(root, file))
        size_limit: int = 100 * 1024 * 1024

        if file_size >= size_limit:
            file_path: str = os.path.join(root, file)
            large_files.append(file_path)

with open(gitignore_path, "w", encoding="utf-8") as gitignore:
    for file in large_files:
        console.print(f"[green]Adding {file}[/]")
        gitignore.write(f"{file}\n")
