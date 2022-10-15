from tkinter import *
from Login_Window import Login_Window

if __name__ == "__main__":

    Window = Tk()
    obj = Login_Window(Window)
    Window.iconbitmap('icon.ico')
    Window.mainloop()