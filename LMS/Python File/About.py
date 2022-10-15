from tkinter import *
from PIL import Image, ImageTk
class About_Class:

    def __init__(self):

        top = Toplevel()
        top.grab_set()
        top.focus_force()

        top.title("Library Management System | About")

        app_width = 700
        app_height = 600

        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-13)}')
        top.resizable(False, False)
        top.iconbitmap('icon.ico')

        img_icon = Image.open(r'logo.png').resize(
            (200, 200), Image.ANTIALIAS)
        photoimage = ImageTk.PhotoImage(img_icon)
        lbl_img_icon = Label(top,image=photoimage)
        lbl_img_icon.place(x=250, y=1)
        
        lbl_Name = Label(top, text="Library Management System", font=(
            "Comic Sans MS", 30, "bold"))
        lbl_Name.place(x=80,y=225)

        lbl_Sub_Name = Label(top, text="A Python Based Desktop GUI Application", font=(
            "Comic Sans MS", 15, "bold"))
        lbl_Sub_Name.place(x=150,y=310)

        Lbl_Dept = Label(top, text="Developed By : Dept. of Computer Science, CMSA, Batch 2019-2022", font=(
            "Comic Sans MS", 14, "bold"))
        Lbl_Dept.place(x=15,y=370)
        
        lbl_Abhi = Label(top, text="Abhisek Midya", font=(
            "Comic Sans MS", 18, "bold"))
        lbl_Abhi.place(x=250,y=420)

        lbl_Atish = Label(top, text="Atish Sarkar", font=(
            "Comic Sans MS", 18, "bold"))
        lbl_Atish.place(x=250,y=540)

        lbl_Avi = Label(top, text="Avijit Halder", font=(
            "Comic Sans MS", 18, "bold"))
        lbl_Avi.place(x=250,y=500)

        lbl_Ahin = Label(top, text="Ahin Subhra Halder", font=(
            "Comic Sans MS", 18, "bold"))
        lbl_Ahin.place(x=250,y=460)

        

        lbl_version = Label(top, text="Version: 2.0", font=(
            "Comic Sans MS", 18, "bold"))
        lbl_version.place(x=540,y=550)

        top.mainloop()
        
        
