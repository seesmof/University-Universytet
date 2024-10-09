from tkinter import *
window=Tk()
window.geometry("700x300")
window.resizable(0,0)
window.configure(background="white")
window.title("Kinoteatr")
window.bind("<Escape>",lambda _:window.destroy())

container=Frame(window,background="white")
container.pack(fill=BOTH,expand=1,padx=7,pady=7)

def clear_container():
    for w in container.winfo_children():w.destroy()

def run(text:str):print(text)

data={"ONE":[[1,2,3],[1,2,3]],"TWO":[[1,2,3],[1,2,3],[1,2,3]]}
for m in data:
    b=Button(container,text=m,command=lambda:run(m))
    b.pack(side=TOP,fill=X)

if __name__=="__main__":window.mainloop()
