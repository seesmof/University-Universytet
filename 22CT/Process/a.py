from rich.console import Console
from rich.traceback import install

install()
console = Console()

Name = "Seth"
MonthlySalary = 12_500
TaxesPercent = 14.5
TaxesAmount = MonthlySalary * TaxesPercent / 100
RawSalary = MonthlySalary - TaxesAmount

console.print(
    f"{Name} has ${MonthlySalary} per month minus {TaxesPercent}% taxes, which is ${TaxesAmount}, so the raw salary is ${RawSalary}."
)

countLines = """
- Name: Adam
- Name: Eve
- Name: Abraham
- Name: Ruth
- Name: Isaac
- Name: Jacob
- Name: Daniel
- Name: Matthew
- Name: Mark
- Name: Luke
- Name: John
- Name: Solomon
"""
lines = countLines.split("\n")

console.print(len(lines))
