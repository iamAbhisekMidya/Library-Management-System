from tkinter import *
from tkinter import ttk, messagebox
import pymysql


class Not_Returned_Book_Class:

    def __init__(self, username, dbpassword):

        def Not_Returned_Book_Clear_Btn(event=""):
            Input_P_cmb_search.current(0)
            self.P_Search.set("")
            Not_Returned_Book_Display_Data()
            Input_P_search.focus()

        def Clear_Display_Data(event=""):
            if self.P_Search.get()=="":
                Not_Returned_Book_Display_Data()

        def Not_Returned_Book_Display_Data(event=""):
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            cur.execute("select s.sr_no,i.ref_no,m.member_id,m.dept,i.book_id,i.book_name,i.book_ed,m.first_name,m.last_name,m.mail,m.mobile,i.issue_date,i.due_date from issue_book as i,member_details as m,serial as s where i.member_id=m.member_id and s.ref_no=i.ref_no and i.return_date IS NULL order by s.sr_no desc;")
            result = cur.fetchall()

            if len(result) != 0:
                self.Not_Returned_Book_table.delete(*self.Not_Returned_Book_table.get_children())

                for row in result:
                    self.Not_Returned_Book_table.insert('', END, values=row)

                sqlCon.commit()
                sqlCon.close()
            else:
                sqlCon.close()
                self.Not_Returned_Book_table.delete(*self.Not_Returned_Book_table.get_children())

        def Not_Returned_Book_Search_Btn(event=""):
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            try:
                if self.P_Search.get() == "":
                    messagebox.showerror(
                        'Library Management System', 'Please Fill The Required Search Input.', parent=top)
                else:
                    if self.Pcmb.get() == "Member Name":
                        Nam = self.P_Search.get().split()
                        cur.execute("select s.sr_no,i.ref_no,m.member_id,m.dept,i.book_id,i.book_name,i.book_ed,m.first_name,m.last_name,m.mail,m.mobile,i.issue_date,i.due_date from issue_book as i,member_details as m,serial as s where i.member_id=m.member_id and s.ref_no=i.ref_no and i.return_date IS NULL and m.first_name like '%" +
                                    Nam[0]+"%' or i.member_id=m.member_id and s.ref_no=i.ref_no and i.return_date IS NULL and m.last_name like '%"+Nam[-1]+"%' order by s.sr_no desc;")
                    elif self.Pcmb.get() == "Member ID":
                        cur.execute("select s.sr_no,i.ref_no,m.member_id,m.dept,i.book_id,i.book_name,i.book_ed,m.first_name,m.last_name,m.mail,m.mobile,i.issue_date,i.due_date from issue_book as i,member_details as m,serial as s where i.member_id=m.member_id and s.ref_no=i.ref_no and i.return_date IS NULL and m.member_id like '%"+self.P_Search.get()+"%' order by s.sr_no desc;")
                    elif self.Pcmb.get() == "Book Name":
                        cur.execute("select s.sr_no,i.ref_no,m.member_id,m.dept,i.book_id,i.book_name,i.book_ed,m.first_name,m.last_name,m.mail,m.mobile,i.issue_date,i.due_date from issue_book as i,member_details as m,serial as s where i.member_id=m.member_id and s.ref_no=i.ref_no and i.return_date IS NULL and i.book_name like '%"+self.P_Search.get()+"%' order by s.sr_no desc;")
                    else:
                        cur.execute("select s.sr_no,i.ref_no,m.member_id,m.dept,i.book_id,i.book_name,i.book_ed,m.first_name,m.last_name,m.mail,m.mobile,i.issue_date,i.due_date from issue_book as i,member_details as m,serial as s where i.member_id=m.member_id and s.ref_no=i.ref_no and i.return_date IS NULL and i.ref_no like '%"+self.P_Search.get()+"%' order by s.sr_no desc;")

                    result = cur.fetchall()

                    if len(result) != 0:
                        self.Not_Returned_Book_table.delete(
                            *self.Not_Returned_Book_table.get_children())

                        for row in result:
                            self.Not_Returned_Book_table.insert('', END, values=row)

                        sqlCon.commit()
                        sqlCon.close()
                    else:
                        sqlCon.close()
                        self.Not_Returned_Book_table.delete(
                            *self.Not_Returned_Book_table.get_children())
                        messagebox.showerror(
                            'Library Management System', 'No Record Found.', parent=top)
            except:
                pass

        self.Pcmb = StringVar()
        self.P_Search = StringVar()

        top = Toplevel()
        top.grab_set()

        top.title("Library Management System | Not Returned Book")

        app_width = 1000
        app_height = 600
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-13)}')
        top.resizable(False, False)
        top.iconbitmap('icon.ico')
        Search_Not_Returned_Book_Frame = Frame(top, bd=10, relief=RIDGE)
        Search_Not_Returned_Book_Frame.place(x=0, y=5, relwidth=1, height=120)

        Search_Not_Returned_Book_Inner_Frame = LabelFrame(Search_Not_Returned_Book_Frame, text="Search Record", fg="green", bd=10, relief=RIDGE,
                                                font=("Comic Sans MS", 10, "bold"))
        Search_Not_Returned_Book_Inner_Frame.place(x=15, y=5, height=85, relwidth=.97)

        Input_P_cmb_search = ttk.Combobox(Search_Not_Returned_Book_Inner_Frame, textvariable=self.Pcmb, values=(
            "Member ID", "Reference No", "Member Name", "Book Name"), cursor="hand2", state="readonly", justify=CENTER, font=("Comic Sans MS", 16, "bold"))
        Input_P_cmb_search.place(x=20, y=10, width=200)
        Input_P_cmb_search.current(0)
        Input_P_search = ttk.Entry(
            Search_Not_Returned_Book_Inner_Frame, textvariable=self.P_Search, font=("Comic Sans MS", 17, "bold"))
        Input_P_search.place(x=240, y=10)
        Input_P_search.focus()
        Input_P_search.bind("<Return>", lambda funct1: Not_Returned_Book_Search_Btn())
        Input_P_search.bind('<KeyRelease>', lambda funct1: Clear_Display_Data())
        btn_P_Search = Button(Search_Not_Returned_Book_Inner_Frame, command=Not_Returned_Book_Search_Btn, text="Search", cursor="hand2", font=(
            "Comic Sans MS", 18, "bold"), bg="#000716", fg="white").place(x=540, y=10, width=180, height=35)
        btn_P_Clear = Button(Search_Not_Returned_Book_Inner_Frame, command=Not_Returned_Book_Clear_Btn, text="Clear", cursor="hand2", font=(
            "Comic Sans MS", 18, "bold"), bg="#000716", fg="white").place(x=740, y=10, width=180, height=35)

        Not_Returned_Book_Frame = Frame(top, bd=10, relief=RIDGE, padx=10)
        Not_Returned_Book_Table_Frame = Frame(
            Not_Returned_Book_Frame, bd=10, relief=RIDGE, padx=0, pady=5)

        Not_Returned_Book_Frame.place(x=0, y=135, height=465, relwidth=1)
        Not_Returned_Book_Table_Frame.place(x=0, y=10, height=425, relwidth=1)

        Not_Returned_Book_Xscroll = Scrollbar(Not_Returned_Book_Table_Frame, orient=HORIZONTAL)
        Not_Returned_Book_Yscroll = Scrollbar(Not_Returned_Book_Table_Frame, orient=VERTICAL)

        self.Not_Returned_Book_table = ttk.Treeview(Not_Returned_Book_Table_Frame, column=("sr_no", "refno", "mid","dpt", "bid", "bname", "bed", "mfname",
                                          "mlname", "mmail", "mmob", "bissu", "bdue"), xscrollcommand=Not_Returned_Book_Xscroll.set, yscrollcommand=Not_Returned_Book_Yscroll.set)

        Not_Returned_Book_Xscroll.pack(side=BOTTOM, fill=X)
        Not_Returned_Book_Yscroll.pack(side=RIGHT, fill=Y)

        Not_Returned_Book_Xscroll.config(command=self.Not_Returned_Book_table.xview)
        Not_Returned_Book_Yscroll.config(command=self.Not_Returned_Book_table.yview)

        self.Not_Returned_Book_table.heading("sr_no", text="Serial No")
        self.Not_Returned_Book_table.heading("refno", text="Reference No")
        self.Not_Returned_Book_table.heading("mid", text="Member Id")
        self.Not_Returned_Book_table.heading("dpt", text="Department")
        self.Not_Returned_Book_table.heading("mfname", text="First Name")
        self.Not_Returned_Book_table.heading("mlname", text="Last Name")
        self.Not_Returned_Book_table.heading("mmail", text="Mail Id")
        self.Not_Returned_Book_table.heading("mmob", text="Mobile No")
        self.Not_Returned_Book_table.heading("bid", text="Book Id")
        self.Not_Returned_Book_table.heading("bname", text="Book Name")
        self.Not_Returned_Book_table.heading("bed", text="Book Edition")
        self.Not_Returned_Book_table.heading("bissu", text="Issue Date")
        self.Not_Returned_Book_table.heading("bdue", text="Due Date")
        self.Not_Returned_Book_table["show"] = "headings"
        self.Not_Returned_Book_table.pack(fill=BOTH, expand=1)

        self.Not_Returned_Book_table.column("sr_no", width=100, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column("refno", width=150, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column("mid", width=150, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column("dpt", width=200, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column(
            "mfname", width=150, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column(
            "mlname", width=150, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column("mmail", width=200, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column("mmob", width=150, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column("bid", width=150, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column("bname", width=200, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column("bed", width=100, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column("bissu", width=100, stretch=0, anchor=CENTER)
        self.Not_Returned_Book_table.column("bdue", width=100, stretch=0, anchor=CENTER)

        Not_Returned_Book_Display_Data()
