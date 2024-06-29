"""
folder names are in the following format:
    yNtN
where N is an integer

this format means the following:
    y - year
    t - term or a semester

so, if we have a folder name of y2t2, we can decipher it as:
Year_2_Term_2
"""

import inquirer
from rich.console import Console
from rich.traceback import install

install()
console = Console()


folder_name: str = inquirer.prompt(
    [
        inquirer.Text(
            "folder name",
            message="Enter the folder name you wanna decrypt",
            validate=lambda _, x: x != "" and "y" in x and "t" in x,
            default="y2t2",
        )
    ]
)["folder name"]

year: str = folder_name[1:2]
term: str = folder_name[3:4]

response: str = f"""
Year: {year}
Term: {term}
[purple]Year_{year}_Term_{term}[/purple]
"""
console.print(response)
