import tkinter
import tkinter.font

window = tkinter.TK()
window.title('가상화폐 금액표시')
window.geometry("400x200")
window.resizable(False,False)

font = tkinter.font.Font(size = 30)
label=tkinter.Label(window, text="hello")

label.pack()

window.mainloop()