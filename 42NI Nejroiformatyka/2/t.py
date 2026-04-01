from tkinter import TOP, Button, Frame, Menu, Tk


def click(e):
    but = e.widget
    i = but.n

    if s[i] == -1:
        s[i] = 1
        but.configure(bg="black")
    else:
        s[i] = -1
        but.configure(bg="white")


def learn():
    m = n * n
    for i in range(m):
        for j in range(i + 1, m):
            w[i][j] = w[i][j] + s[i] * s[j]
            w[j][i] = w[i][j]


def recall():
    m = n * n
    c = 1
    while c != 0:
        c = 0
        for i in range(m):
            a = 0
            for j in range(m):
                a = a + s[j] * w[i][j]
            if a < 0 and s[i] > 0:
                s[i] = -1
                c = 1
            if a > 0 and s[i] < 0:
                s[i] = 1
                c = 1
    update()


def update():
    for key, but in grid_frame.children.items():
        i = but.n
        if s[i] == -1:
            but.configure(bg="white")
        else:
            but.configure(bg="black")


if __name__ == "__main__":
    n = 8
    s = [-1 for i in range(n * n)]
    w = [[0 for j in range(n * n)] for i in range(n * n)]
    root = Tk()
    root.title("Hopfield")
    menu_bar = Menu(root)
    root.config(menu=menu_bar)
    menu_bar.add_command(label="learn", command=learn)
    menu_bar.add_command(label="recall", command=recall)
    grid_frame = Frame(root)
    grid_frame.pack(side=TOP)
    for r in range(8):
        for c in range(8):
            button = Button(grid_frame, text="    ", borderwidth=1, bg="white")
            button.n = c + r * 8
            button.grid(row=r, column=c)
            button.bind("<Button-1>", click)
    root.mainloop()
