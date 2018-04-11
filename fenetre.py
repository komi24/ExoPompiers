from tkinter import *
from functools import partial

def printHello(i,j):
    print("Hello",i)

fenetre = Tk(className="Mon titre")

fenetre.geometry("500x400")

frame1 = Frame(fenetre)
label =  Label(frame1, text="Hello Toulouse !! TOP")
label.pack(side=TOP, padx=5, pady=8)
frame1.pack(side=TOP)
# label1 =  Label(fenetre, text="Hello Toulouse !! LEFT")
# label1.pack(side=LEFT)
# button2 =  Button(fenetre, text="Mon Bouton Bottom")
# button2.pack(side=BOTTOM)
# frame2 = Frame(fenetre)
# for i in range(8):
#     for j in range(8):
#         b = Button(frame2, text="%s %s"%(i,j))
#         b.grid(row=i, column=j)
#         fonction = partial(printHello, i, j)
#         b.bind("<Button-1>", lambda e:fonction())

frame2 = Frame(fenetre)
mon_canvas = Canvas(frame2, width=300, height=300, bg='white')
mon_canvas.pack(side=TOP)

img= PhotoImage(file="pompier.gif")

mon_canvas.create_image(20,20,image=img)

frame2.pack(side=TOP)
fenetre.mainloop()