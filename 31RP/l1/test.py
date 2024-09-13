import tkinter as tk

root = tk.Tk()

listbox = tk.Listbox(root)
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.pack()

combobox = tk.StringVar(root)
combobox.set("Select...")
options = ["Option 1", "Option 2"]
drop = tk.OptionMenu(root, combobox, *options)
drop.pack()

root.mainloop()
