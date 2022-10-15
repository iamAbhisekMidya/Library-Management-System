from tkinter import *
from tkinter import ttk, messagebox
import pymysql


class Particular_User_Record_Class:

    def __init__(self, username, dbpassword):

        def User_Clear_Btn(event=""):
            Input_P_cmb_search.current(0)
            self.P_Search.set("")
            self.Member_Type.set("")
            self.Member_ID.set("")
            self.First_Name.set("")
            self.Last_Name.set("")
            self.Address.set("")
            self.Department.set("")
            self.Mail.set("")
            self.Ph.set("")
            self.Cur_Amount.set("")
            self.B_Count.set("")
            self.User_table.delete(*self.User_table.get_children())
            Input_P_search.focus()

        def User_Search_Btn(event=""):
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            try:
                if self.P_Search.get() == "":
                    messagebox.showerror(
                        'Library Management System', 'Please Fill The Required Search Input.', parent=top)
                else:
                    if self.Pcmb.get() == "Mail Id":
                        cur.execute("select s.sr_no,i.ref_no,i.book_id,i.book_name,i.book_ed,b.book_sub,b.author,i.issue_date,i.due_date,i.return_date from issue_book as i,member_details as m,serial as s,books_details as b where i.member_id=m.member_id and s.ref_no=i.ref_no and i.book_name=b.book_name and m.mail='" + self.P_Search.get()+"'order by s.sr_no desc;")
                    elif self.Pcmb.get() == "Member ID":
                        cur.execute("select s.sr_no,i.ref_no,i.book_id,i.book_name,i.book_ed,b.book_sub,b.author,i.issue_date,i.due_date,i.return_date from issue_book as i,member_details as m,serial as s,books_details as b where i.member_id=m.member_id and s.ref_no=i.ref_no and i.book_name=b.book_name and m.member_id='" + self.P_Search.get()+"'order by s.sr_no desc;")

                    else:
                        cur.execute("select s.sr_no,i.ref_no,i.book_id,i.book_name,i.book_ed,b.book_sub,b.author,i.issue_date,i.due_date,i.return_date from issue_book as i,member_details as m,serial as s,books_details as b where i.member_id=m.member_id and s.ref_no=i.ref_no and i.book_name=b.book_name and m.mobile='" + self.P_Search.get()+"'order by s.sr_no desc;")

                    result = cur.fetchall()
                    count = 0
                    if len(result) != 0:
                        self.User_table.delete(
                            *self.User_table.get_children())

                        for row in result:
                            self.User_table.insert('', END, values=row)
                            count = count+1

                        sqlCon.commit()
                        sqlCon.close()
                    else:
                        self.User_table.delete(*self.User_table.get_children())

                    sqlCon = pymysql.connect(
                        host="localhost", user=username, password=dbpassword, database="lms")
                    cur = sqlCon.cursor()
                    if self.Pcmb.get() == "Mail Id":
                        cur.execute(
                            "select * from member_details where mail=%s;", (self.P_Search.get()))
                    elif self.Pcmb.get() == "Member ID":
                        cur.execute(
                            "select * from member_details where member_id=%s;", (self.P_Search.get()))
                    else:
                        cur.execute(
                            "select * from member_details where mobile=%s;", (self.P_Search.get()))

                    result = cur.fetchall()
                    if len(result) != 0:
                        for row in result:
                            self.Member_Type.set(row[0])
                            self.Member_ID.set(row[1])
                            self.First_Name.set(row[2])
                            self.Last_Name.set(row[3])
                            self.Address.set(row[4])
                            self.Department.set(row[5])
                            self.Mail.set(row[6])
                            self.Ph.set(row[7])
                            self.Cur_Amount.set(row[8])
                            self.B_Count.set(count)
                        sqlCon.close()
                    else:
                        self.Member_Type.set("")
                        self.Member_ID.set("")
                        self.First_Name.set("")
                        self.Last_Name.set("")
                        self.Address.set("")
                        self.Department.set("")
                        self.Mail.set("")
                        self.Ph.set("")
                        self.Cur_Amount.set("")
                        sqlCon.close()
                        User_Clear_Btn()
                        messagebox.showerror(
                            'Library Management System', 'No Record Found.', parent=top)
                        return

            except:
                pass

        self.Pcmb = StringVar()
        self.P_Search = StringVar()
        self.Member_Type = StringVar()
        self.Member_ID = StringVar()
        self.First_Name = StringVar()
        self.Last_Name = StringVar()
        self.Address = StringVar()
        self.Department = StringVar()
        self.Mail = StringVar()
        self.Ph = StringVar()
        self.Cur_Amount = StringVar()
        self.cr_Number = StringVar()
        self.B_Count = StringVar()

        top = Toplevel()
        top.grab_set()

        top.title("Library Management System | User Details")

        app_width = 1000
        app_height = 600
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-13)}')
        top.resizable(False, False)
        top.iconbitmap('icon.ico')
        

        Search_User_Frame = Frame(top, bd=10, relief=RIDGE)
        Search_User_Frame.place(x=0, y=5, relwidth=1, height=120)

        Search_User_Inner_Frame = LabelFrame(Search_User_Frame, text="Search Record", fg="green", bd=10, relief=RIDGE,
                                             font=("Comic Sans MS", 10, "bold"))
        Search_User_Inner_Frame.place(x=15, y=5, height=85, relwidth=.97)

        Input_P_cmb_search = ttk.Combobox(Search_User_Inner_Frame, textvariable=self.Pcmb, values=(
            "Member ID", "Mail Id", "Phone No"), cursor="hand2", state="readonly", justify=CENTER, font=("Comic Sans MS", 16, "bold"))

        Input_P_cmb_search.place(x=20, y=10, width=200)
        Input_P_cmb_search.current(0)
        Input_P_search = ttk.Entry(
            Search_User_Inner_Frame, textvariable=self.P_Search, font=("Comic Sans MS", 16, "bold"))
        Input_P_search.place(x=240, y=10)
        Input_P_search.focus()
        Input_P_search.bind("<Return>", lambda funct1: User_Search_Btn())
        btn_P_Search = Button(Search_User_Inner_Frame, command=User_Search_Btn, text="Search", cursor="hand2", font=(
            "Comic Sans MS", 16, "bold"), bg="#000716", fg="white").place(x=530, y=10, width=170, height=35)
        btn_P_Clear = Button(Search_User_Inner_Frame, command=User_Clear_Btn, text="Clear", cursor="hand2", font=(
            "Comic Sans MS", 16, "bold"), bg="#000716", fg="white").place(x=730, y=10, width=170, height=35)

        UR_Outer_Frame = Frame(top, bd=10, relief=RIDGE, padx=10)

        UR_Outer_Frame.place(x=0, y=130, height=255, relwidth=1)

        UR_Inner_Frame = LabelFrame(UR_Outer_Frame, text="Members Information", fg="green", bd=10, relief=RIDGE,
                                    font=("Comic Sans MS", 10, "bold"), padx=0)

        UR_Inner_Frame.place(x=0, y=0, height=230, relwidth=1)

        Lbl_Member_Type = Label(UR_Inner_Frame, text="Member Type:", font=(
            "Comic Sans MS", 13, "bold"), padx=20, pady=4).grid(row=0, column=0, sticky=W)
        Input_Member_Type = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", 14, "bold"), width=24, textvariable=self.Member_Type).grid(row=0, column=1, sticky=W)

        Lbl_Member_ID = Label(UR_Inner_Frame, text="Member ID:", font=(
            "Comic Sans MS", 13, "bold"), padx=20, pady=4).grid(row=1, column=0, sticky=W)
        Input_Member_ID = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", 14, "bold"), width=24, textvariable=self.Member_ID)
        Input_Member_ID.grid(row=1, column=1, sticky=W)

        Lbl_First_Name = Label(UR_Inner_Frame, text="First Name:", font=(
            "Comic Sans MS", 13, "bold"), padx=20, pady=4).grid(row=2, column=0, sticky=W)
        Input_First_Name = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", 14, "bold"), width=24, textvariable=self.First_Name).grid(row=2, column=1, sticky=W)

        Lbl_Last_Name = Label(UR_Inner_Frame, text="Last Name:", font=(
            "Comic Sans MS", 13, "bold"), padx=20, pady=4).grid(row=3, column=0, sticky=W)
        Input_Last_Name = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", 14, "bold"), width=24, textvariable=self.Last_Name).grid(row=3, column=1, sticky=W)

        Lbl_Address = Label(UR_Inner_Frame, text="Address:", font=(
            "Comic Sans MS", 13, "bold"), padx=20, pady=4).grid(row=4, column=0, sticky=W)
        Input_Address = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", 14, "bold"), width=24, textvariable=self.Address).grid(row=4, column=1, sticky=W)

        Lbl_Department = Label(UR_Inner_Frame, text="Department:", font=(
            "Comic Sans MS", 13, "bold"), padx=20, pady=4).grid(row=0, column=2, sticky=W)
        Input_Department = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", 14, "bold"), width=24, textvariable=self.Department).grid(row=0, column=3, sticky=W)

        Lbl_Mail = Label(UR_Inner_Frame, text="Mail ID:", font=(
            "Comic Sans MS", 13, "bold"), padx=20, pady=4).grid(row=1, column=2, sticky=W)
        Input_Mail = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", 14, "bold"), width=24, textvariable=self.Mail).grid(row=1, column=3, sticky=W)

        Lbl_PH = Label(UR_Inner_Frame, text="Mobile Number:", font=(
            "Comic Sans MS", 13, "bold"), padx=20, pady=4).grid(row=2, column=2, sticky=W)
        Input_PH = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", 14, "bold"), width=24, textvariable=self.Ph).grid(row=2, column=3, sticky=W)

        Lbl_Cur_Amount = Label(UR_Inner_Frame, text="Balance:", font=(
            "Comic Sans MS", 13, "bold"), padx=20, pady=4).grid(row=3, column=2, sticky=W)
        Input_Cur_Amount = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", 14, "bold"), width=24, textvariable=self.Cur_Amount).grid(row=3, column=3, sticky=W)
        Lbl_B_Count = Label(UR_Inner_Frame, text="Book Count:", font=(
            "Comic Sans MS", 13, "bold"), padx=20, pady=4).grid(row=4, column=2, sticky=W)
        Input_B_Count = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", 14, "bold"), width=24, textvariable=self.B_Count).grid(row=4, column=3, sticky=W)

        Tb_Frame = Frame(top, bd=10, relief=RIDGE, padx=10)
        User_Table_Frame = Frame(
            Tb_Frame, bd=10, relief=RIDGE, padx=0, pady=5)

        Tb_Frame.place(x=0, y=390, height=210, relwidth=1)
        User_Table_Frame.place(x=0, y=10, height=170, relwidth=1)

        User_Xscroll = Scrollbar(User_Table_Frame, orient=HORIZONTAL)
        User_Yscroll = Scrollbar(User_Table_Frame, orient=VERTICAL)

        self.User_table = ttk.Treeview(User_Table_Frame, column=("sr_no", "refno", "bid", "bname", "bed", "bsub",
                                       "bauth", "bissu", "bdue", "bret"), xscrollcommand=User_Xscroll.set, yscrollcommand=User_Yscroll.set)

        User_Xscroll.pack(side=BOTTOM, fill=X)
        User_Yscroll.pack(side=RIGHT, fill=Y)

        User_Xscroll.config(command=self.User_table.xview)
        User_Yscroll.config(command=self.User_table.yview)

        self.User_table.heading("sr_no", text="Serial No")
        self.User_table.heading("refno", text="Reference No")
        self.User_table.heading("bid", text="Book Id")
        self.User_table.heading("bname", text="Book Name")
        self.User_table.heading("bed", text="Book Edition")
        self.User_table.heading("bsub", text="Book Subject")
        self.User_table.heading("bauth", text="Book Author")
        self.User_table.heading("bissu", text="Issue Date")
        self.User_table.heading("bdue", text="Due Date")
        self.User_table.heading("bret", text="Returned Date")

        self.User_table.column("sr_no", width=100, stretch=0, anchor=CENTER)
        self.User_table.column("refno", width=150, stretch=0, anchor=CENTER)
        self.User_table.column("bid", width=150, stretch=0, anchor=CENTER)
        self.User_table.column("bname", width=200, stretch=0, anchor=CENTER)
        self.User_table.column("bed", width=100, stretch=0, anchor=CENTER)
        self.User_table.column("bsub", width=100, stretch=0, anchor=CENTER)
        self.User_table.column("bauth", width=150, stretch=0, anchor=CENTER)
        self.User_table.column("bissu", width=100, stretch=0, anchor=CENTER)
        self.User_table.column("bdue", width=100, stretch=0, anchor=CENTER)
        self.User_table.column("bret", width=100, stretch=0, anchor=CENTER)

        self.User_table["show"] = "headings"
        self.User_table.pack(fill=BOTH, expand=1)
    
