from tkinter import*
#https://www.youtube.com/watch?v=Cq5tpTwfJJY закончил на 10 41
root =Tk()
root.title('y = sin(x)')
root.geometry('1020x620')

canvas = Canvas(root, width=1020, height=620, bg='#002')

# линия ссетки по вертикали
for y in range(21):
    k = 50 * y
    canvas.create_line(10+k, 610, 10+k, 10, widht=1, fill='#191938')

# нилия сетки по горизонтали
for x in range(13):
    k = 50 * x
    canvas.create_line(10, 10+k, 1010, 10+k, widht=1, fill='#191938')

canvas.pack()
root.mainloop()
