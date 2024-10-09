from tkinter import *
window=Tk()
window.geometry("700x300")
window.resizable(0,0)
window.configure(background="white")
window.title("Kinoteatr")
window.bind("<Escape>",lambda _:window.destroy())
if __name__=="__main__":window.mainloop()