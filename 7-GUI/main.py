import tkinter 

window = tkinter.Tk()

"""
    Geometria Pack
    La usaremos para situar elementos de arriba a abajo
    o cara a cara.
"""
label_greeting = tkinter.Label(window, text='Hola!', bg='yellow', fg='blue' )
label_greeting.pack(ipadx=30, ipady=30, side='left')

label_bye =tkinter.Label(window,text='bye', bg='blue', fg='white')
label_bye.pack(ipadx=40, ipady=30, side='right')
window.mainloop()

