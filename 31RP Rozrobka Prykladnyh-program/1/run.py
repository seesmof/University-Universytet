from tkinter import *
window=Tk()
window.geometry("700x300")
window.resizable(0,0)
window.configure(background="white")
window.title("Kinoteatr")
window.bind("<Escape>",lambda _:window.destroy())

container=Frame(window,background="white")
container.pack(fill=BOTH,expand=1,padx=7,pady=7)

movies=["JESUS"]
for m in movies:
    b=Button(container,text=m)
    b.pack(side=TOP,fill=X)

if __name__=="__main__":window.mainloop()