from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from PIL import Image, ImageTk
from Admin_Panel import Admin_Panel_Class
from User_Panel import User_Panel_Class


class Login_Window:
    '''This is the Class where we take Input the Username & Password of the MySQL server and
    after Proper Connection it Redirect to another class. After that this class would be destroyed.'''

    def __init__(self, root):
        '''This is the Constructor of Login_Window class'''

        def my_show():
            '''Method for Show / Hide Password'''

            if(self.showpass.get() == 1):
                Input_Password.config(show='')
            else:
                Input_Password.config(show='*')

        def login():
            '''Method for Login Button'''

            if self.Username.get() == "":
                messagebox.showerror(
                    'Library Management System', 'Please Fill Username')
                Input_Username.focus()

            elif self.Username.get().lower() != "" and self.Username.get().isnumeric():
                
                sqlCon = pymysql.connect(
                    host="localhost", user="user", password="1234",database="lms")
                
                cur = sqlCon.cursor()
                cur.execute("select password from member_details where member_id=%s;", (self.Username.get()))
                result = cur.fetchall()
                
                if len(result) != 0:
                    for row in result:
                        pw=(row[0])
                
                
                else:
                    sqlCon.close()
                    messagebox.showerror(
                    'Library Management System', 'Username Not Found.')
                    Input_Username.focus()
                    return
                
                if pw==self.Password.get():

                    sqlCon.close()

                    root.destroy()
                    '''If Entered Username and Password got matched then destroy the login Window
                    and Opening the main Window.'''

                    User_Window = Tk()

                    obj1 = User_Panel_Class(
                        User_Window, self.Username.get())

                    User_Window.iconbitmap('icon.ico')

                    User_Window.mainloop()
                else:
                    messagebox.showerror(
                    'Library Management System', 'Wrong Password Entered.')
                    Input_Username.focus()

            elif self.Username.get().lower() != "" and self.Username.get().isalpha():

                try:
                    sqlCon = pymysql.connect(
                        host="localhost", user=self.Username.get(), password=self.Password.get())
                    sqlCon.close()

                    root.destroy()
                    '''If Entered Username and Password got matched then destroy the login Window
                    and Opening the main Window.'''

                    Admin_Window = Tk()

                    obj2 = Admin_Panel_Class(
                        Admin_Window, self.Username.get(), self.Password.get())

                    Admin_Window.iconbitmap('icon.ico')

                    Admin_Window.mainloop()

                except:
                    messagebox.showerror(
                        'Library Management System', 'Please Enter Valid Username and Password')
                    Input_Username.focus()

        self.Username = StringVar()
        self.Password = StringVar()
        self.root = root
        self.showpass = IntVar(value=0)
        '''This Three variable are the Instance Variable of Login_window class'''

        self.root.title("Library Management System | Login Window ")

        app_width = 600
        app_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-50)}')
        self.root.resizable(False, False)

        frame = Frame(self.root)
        frame.place(relheight=1, relwidth=1)
        '''Frame Setting'''

        img_icon = Image.open(r'User_Icon.png').resize(
            (200, 200), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img_icon)
        lbl_img_icon = Label(image=self.photoimage)
        lbl_img_icon.place(x=200, y=1)
        '''Login Window Icon (Logo)'''

        s = ttk.Style()
        s.configure('TCheckbutton', font=("Comic Sans MS", 12))
        s.configure('TButton', font=("Comic Sans MS", 14))
        '''Changing style of button and checkbox'''

        Lbl_Username = ttk.Label(frame, text="Username:", font=(
            "Comic Sans MS", 20, "bold")).place(x=50, y=250)
        Input_Username = ttk.Entry(frame, font=(
            "Comic Sans MS", 18, "bold"), textvariable=self.Username)
        Input_Username.place(x=240, y=250)
        Input_Username.focus()
        Input_Username.bind("<Return>", lambda funct1: Input_Password.focus())
        '''Creating Entry object for taking input (Username) from user'''

        Lbl_Password = ttk.Label(frame, text="Password:", font=(
            "Comic Sans MS", 20, "bold")).place(x=50, y=300)
        Input_Password = ttk.Entry(
            frame, show='*', font=("Comic Sans MS", 18, "bold"), textvariable=self.Password)
        Input_Password.place(x=240, y=300)
        Input_Password.bind('<Return>', lambda event: login())
        '''Creating Entry object for taking input (Password) from user'''

        Showpassword_Btn = ttk.Checkbutton(frame, text='Show Password', cursor="hand2",
                                           variable=self.showpass, onvalue=1, offvalue=0, command=my_show).place(x=238, y=350)
        '''Show / Hide Password Button'''

        Btn_Login = ttk.Button(
            frame, text="Login", cursor="hand2", command=login).place(x=240, y=400)
        '''Login Button'''
