from tkinter import *
from tkinter import ttk, messagebox
import pymysql


class Book_Record_Class:

    def __init__(self, username, dbpassword):

        def Book_Clear_Btn(event=""):
            Input_P_cmb_search.current(0)
            self.P_Search.set("")
            Book_Display_Data()
            Input_P_search.focus()

        def Book_Display_Data(event=""):
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            cur.execute("select * from books_details order by book_name;")
            result = cur.fetchall()

            if len(result) != 0:
                self.Book_table.delete(*self.Book_table.get_children())

                for row in result:
                    self.Book_table.insert('', END, values=row)

                sqlCon.commit()
                sqlCon.close()
            else:
                sqlCon.close()
                self.Book_table.delete(*self.Book_table.get_children())

        def Book_Search_Btn(event=""):
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            try:
                if self.P_Search.get() == "":
                    messagebox.showerror(
                        'Library Management System', 'Please Fill The Required Search Input.', parent=top)
                else:
                    if self.Pcmb.get() == "Book Name":
                        Nam = self.P_Search.get().split()
                        cur.execute("select * from books_details where book_name like '%" +
                                    Nam[0]+"%'order by id_counter;")
                    elif self.Pcmb.get() == "Book Subject":
                        Nam = self.P_Search.get().split()
                        cur.execute("select * from books_details where book_sub like '%" +
                                    Nam[0]+"%'order by id_counter;")
                    elif self.Pcmb.get() == "Author":
                        Nam = self.P_Search.get().split()
                        cur.execute("select * from books_details where author like '%" +
                                    Nam[0]+"%'order by id_counter;")    
                  
                    result = cur.fetchall()

                    if len(result) != 0:
                        self.Book_table.delete(
                            *self.Book_table.get_children())

                        for row in result:
                            self.Book_table.insert('', END, values=row)

                        sqlCon.commit()
                        sqlCon.close()
                    else:
                        sqlCon.close()
                        self.Book_table.delete(
                            *self.Book_table.get_children())
                        messagebox.showerror(
                            'Library Management System', 'No Record Found.', parent=top)
            except:
                pass

        self.Pcmb = StringVar()
        self.P_Search = StringVar()

        top = Toplevel()
        top.grab_set()

        top.title("Library Management System | All Books Records")

        app_width = 1000
        app_height = 600
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-13)}')
        top.resizable(False, False)
        top.iconbitmap('icon.ico')
        Search_Book_Frame = Frame(top, bd=10, relief=RIDGE)
        Search_Book_Frame.place(x=0, y=5, relwidth=1, height=120)

        Search_Book_Inner_Frame = LabelFrame(Search_Book_Frame, text="Search Record", fg="#000716", bd=10, relief=RIDGE,
                                                font=("Comic Sans MS", 10, "bold"))
        Search_Book_Inner_Frame.place(x=15, y=5, height=85, relwidth=.97)

        Input_P_cmb_search = ttk.Combobox(Search_Book_Inner_Frame, textvariable=self.Pcmb, values=(
            "Book Name","Book Subject", "Author"), cursor="hand2", state="readonly", justify=CENTER, font=("Comic Sans MS", 16, "bold"))
        Input_P_cmb_search.place(x=20, y=10, width=200)
        Input_P_cmb_search.current(0)
        Input_P_search = ttk.Entry(
            Search_Book_Inner_Frame, textvariable=self.P_Search, font=("Comic Sans MS", 17, "bold"))
        Input_P_search.place(x=240, y=10)
        Input_P_search.focus()
        Input_P_search.bind("<Return>", lambda funct1: Book_Search_Btn())
        btn_P_Search = Button(Search_Book_Inner_Frame, command=Book_Search_Btn, text="Search", cursor="hand2", font=(
            "Comic Sans MS", 18, "bold"), bg="#000716", fg="white").place(x=540, y=10, width=180, height=35)
        btn_P_Clear = Button(Search_Book_Inner_Frame, command=Book_Clear_Btn, text="Clear", cursor="hand2", font=(
            "Comic Sans MS", 18, "bold"), bg="#000716", fg="white").place(x=740, y=10, width=180, height=35)

        Book_Frame = Frame(top, bd=10, relief=RIDGE, padx=10)
        Book_Table_Frame = Frame(
            Book_Frame, bd=10, relief=RIDGE, padx=0, pady=5)

        Book_Frame.place(x=0, y=135, height=465, relwidth=1)
        Book_Table_Frame.place(x=0, y=10, height=425, relwidth=1)

        Book_Xscroll = Scrollbar(Book_Table_Frame, orient=HORIZONTAL)
        Book_Yscroll = Scrollbar(Book_Table_Frame, orient=VERTICAL)

        self.Book_table = ttk.Treeview(Book_Table_Frame, column=("bn", "bs", "au","sfn", "tob", "rnb"), xscrollcommand=Book_Xscroll.set, yscrollcommand=Book_Yscroll.set)

        Book_Xscroll.pack(side=BOTTOM, fill=X)
        Book_Yscroll.pack(side=RIGHT, fill=Y)

        Book_Xscroll.config(command=self.Book_table.xview)
        Book_Yscroll.config(command=self.Book_table.yview)

        self.Book_table.heading("bn", text="Book Name")
        self.Book_table.heading("bs", text="Book Subject")
        self.Book_table.heading("au", text="Author")
        self.Book_table.heading("sfn", text="Bookshelf No")
        self.Book_table.heading("tob", text="Total Books")
        self.Book_table.heading("rnb", text="Remaining No of Books")

       
        self.Book_table["show"] = "headings"
        self.Book_table.pack(fill=BOTH, expand=1)

        self.Book_table.column("bn", width=400, stretch=0,anchor=CENTER)
        self.Book_table.column("bs", width=200, stretch=0, anchor=CENTER)
        self.Book_table.column("au", width=200, stretch=0, anchor=CENTER)
        self.Book_table.column("sfn", width=100, stretch=0, anchor=CENTER)
        self.Book_table.column(
            "tob", width=150, stretch=0, anchor=CENTER)
        self.Book_table.column(
            "rnb", width=150, stretch=0, anchor=CENTER)

        Book_Display_Data()
