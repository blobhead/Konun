import tkinter as tk
from tkinter import Menu
window = tk.Tk()
window.title('Konun Booter')
window.geometry("500x200")
window.configure(bg='Cyan')

menubar = Menu(window)
window.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu2 = Menu(menubar, tearoff=False)
file_menu.add_command(
    label='Exit',
    command=root.destroy
)
file_menu2.add_command(
    label='Extra'
)
menubar.add_cascade(
    label="Menu",
    menu=file_menu
)
menubar.add_cascade(
    label="Run",
    menu=file_menu2
)

window.mainloop()
