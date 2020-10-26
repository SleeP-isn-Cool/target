import tkinter

canvas = tkinter.Canvas(width=640,height=640)

canvas.pack()

x, y = 320, 330

canvas.create_oval(x-150, y-150, x+150, y+150, fill="black")

canvas.create_oval(x-110, y-110, x+110, y+110, fill="aqua")

canvas.create_oval(x-80, y-80, x+80, y+80, fill="red")

canvas.create_oval(x-50, y-50, x+50, y+50, fill="yellow")

canvas.create_oval(x-10, y-10, x+10, y+10, fill="lime")

canvas.create_oval(x-190, y-190, x+190, y+190, outline="black")

canvas.create_text(x-0, y-0, text="+")

canvas.mainloop()
