import tkinter 
from tkinter import ttk

window = tkinter.Tk()

"""
    Geometria Pack
    La usaremos para situar elementos de arriba a abajo
    o cara a cara.
"""
# label_greeting = tkinter.Label(window, text='Hola!', bg='yellow', fg='blue' )
# label_greeting.pack(ipadx=30, ipady=30, side='left')

# label_bye =tkinter.Label(window,text='bye', bg='blue', fg='white')
# label_bye.pack(ipadx=40, ipady=30, side='right')

window.columnconfigure(0, weight=1)
window.columnconfigure(1,weight=3)


label = ttk.Label

# Etiqueta usuario
username_label =ttk.Label(window, text='Username: ')
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

# Campo usuario
username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5) 


# Etiqueta password
password_label =ttk.Label(window, text='Password: ')
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# Campo password
password_entry = ttk.Entry(window, show='-')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)


#Boton
login_button = ttk.Button(window)
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()

