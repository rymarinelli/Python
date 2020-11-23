from tkinter import *
window = Tk()
window.title("Main Frame")
window.geometry("200x50")

text = Label(window, text="Hello World")
button1 = Button(window, text='Press Me!')


CheckVar1 = IntVar()
CheckVar2 = StringVar()
CheckVar3  = DoubleVar()


C1 = Checkbutton(window, text = "Rap", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
    
C2 = Checkbutton(window, text = "Jazz", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)

C3 = Checkbutton(window, text = "Pop", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)


    
listbox = Listbox(window)
for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)
    

button2 = Radiobutton(window, text="Option 1",
                           variable= CheckVar1, value=1)

button3 = Radiobutton(window, text="Option 2",
                           variable= CheckVar1, value=1)

button4 = Radiobutton(window, text="Option 3",
                           variable= CheckVar1, value=1)


CheckVar2.set("Hey!? How are you doing?")

label = Message( window, textvariable= CheckVar2, relief=RAISED )

scale = Scale( window, variable = CheckVar3 )


text = Text(window)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")

spinBox  = Spinbox(window, from_=0, to=10)


spinBox.pack()

listbox.pack()
   
C1.pack()
C2.pack()
C3.pack()

text.pack()

button1.pack()
button2.pack()
button3.pack()
button4.pack()

label.pack()
text.pack()

scale.pack()

spinBox.pack()

 
window.mainloop()