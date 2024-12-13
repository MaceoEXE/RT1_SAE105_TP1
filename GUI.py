from tkinter import *   #library for an easy GUI
from tkinter import ttk #add on of the previous Lib
from EvoIm import *
from EvoTot import *

window = Tk()
window.geometry("500x300")
window.title("Auxerre population évolution") #name our program window

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1,text="aglommération immédiate")
tab_control.add(tab2,text="aglommération totale")

def Click1():
    Txt2008 = Label(tab1, text="Habitants en 2008:")
    Txt2008.place(x=10, y=40)
    Im2008 = Label(tab1, text=ImTot2008)
    Im2008.place(x=120, y=40)
    
    Txt2016 = Label(tab1, text="Habitants en 2016:")
    Txt2016.place(x=10, y=80)
    Im2016 = Label(tab1, text=ImTot2016)
    Im2016.place(x=120, y=80)

    Txt2021 = Label(tab1, text="Habitants en 2021:")
    Txt2021.place(x=10, y=120)
    Im2021 = Label(tab1, text=ImTot2021)
    Im2021.place(x=120, y=120)

    Txt2023 = Label(tab1, text="Habitants en 2023:")
    Txt2023.place(x=10, y=160)
    Im2023 = Label(tab1, text=ImTot2023)
    Im2023.place(x=120, y=160)
    
    graphIm()


def Click2():
    ToTot2008 = Label(tab2, text=Tot2008)
    ToTot2008.place(x=120, y=40)
    ToTxt2008 = Label(tab2, text="Habitants en 2008:")
    ToTxt2008.place(x=10, y=40)
    
    ToTot2016 = Label(tab2, text=Tot2016)
    ToTot2016.place(x=120, y=80)
    ToTxt2016 = Label(tab2, text="Habitants en 2016:")
    ToTxt2016.place(x=10, y=80)

    ToTot2021 = Label(tab2, text=Tot2021)
    ToTot2021.place(x=120, y=120)
    ToTxt2021 = Label(tab2, text="Habitants en 2021:")
    ToTxt2021.place(x=10, y=120)
    
    ToTot2023 = Label(tab2, text=Tot2023)
    ToTot2023.place(x=120, y=160)
    ToTxt2023 = Label(tab2, text="Habitants en 2023:")
    ToTxt2023.place(x=10, y=160)
    
    graphTot()

btn1 = Button(tab1,text="évolution aglommération immédiate", command=Click1)
btn1.place(x=10,y=10)
btn2 = Button(tab2,text="évolution aglommération totale", command=Click2)
btn2.place(x=10,y=10)

tab_control.pack(expand=1, fill='both')

window.mainloop()