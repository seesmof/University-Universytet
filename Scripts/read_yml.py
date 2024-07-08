import os
import yaml
from rich.console import Console
from rich.traceback import install

install()
console = Console()

from constants import Constants as c

base_dir: str = c.DOCS_DIR
target_file: str = os.path.join(base_dir, "class_times.yml")

with open(target_file, "r", encoding="utf-8") as file:
    input_data: dict = yaml.safe_load(file)

console.print(input_data)
