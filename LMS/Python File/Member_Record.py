from tkinter import *
from tkinter import ttk, messagebox
import pymysql


class Member_Record_Class:

    def __init__(self, username, dbpassword):

        def Member_Clear_Btn(event=""):
            Input_P_cmb_search.current(0)
            self.P_Search.set("")
            Member_Display_Data()
            Input_P_search.focus()

        def Member_Display_Data(event=""):
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            cur.execute("select * from member_details order by member_id ;")
            result = cur.fetchall()

            if len(result) != 0:
                self.Member_table.delete(*self.Member_table.get_children())

                for row in result:
                    self.Member_table.insert('', END, values=row)

                sqlCon.commit()
                sqlCon.close()
            else:
                sqlCon.close()
                self.Member_table.delete(*self.Member_table.get_children())

        def Member_Search_Btn(event=""):
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
                        cur.execute("select * from member_details where first_name like '%" +
                                    Nam[0]+"%' or last_name like '%"+Nam[-1]+"%' order by member_id;")
                    elif self.Pcmb.get() == "Member ID":
                        cur.execute("select * from member_details where member_id like '%"+self.P_Search.get()+"%';")
                  
                    result = cur.fetchall()

                    if len(result) != 0:
                        self.Member_table.delete(
                            *self.Member_table.get_children())

                        for row in result:
                            self.Member_table.insert('', END, values=row)

                        sqlCon.commit()
                        sqlCon.close()
                    else:
                        sqlCon.close()
                        self.Member_table.delete(
                            *self.Member_table.get_children())
                        messagebox.showerror(
                            'Library Management System', 'No Record Found.', parent=top)
            except:
                pass

        self.Pcmb = StringVar()
        self.P_Search = StringVar()

        top = Toplevel()
        top.grab_set()

        top.title("Library Management System | All Members Records")

        app_width = 1000
        app_height = 600
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-13)}')
        top.resizable(False, False)
        top.iconbitmap('icon.ico')
        Search_Member_Frame = Frame(top, bd=10, relief=RIDGE)
        Search_Member_Frame.place(x=0, y=5, relwidth=1, height=120)

        Search_Member_Inner_Frame = LabelFrame(Search_Member_Frame, text="Search Record", fg="green", bd=10, relief=RIDGE,
                                                font=("Comic Sans MS", 10, "bold"))
        Search_Member_Inner_Frame.place(x=15, y=5, height=85, relwidth=.97)

        Input_P_cmb_search = ttk.Combobox(Search_Member_Inner_Frame, textvariable=self.Pcmb, values=(
            "Member ID", "Member Name"), cursor="hand2", state="readonly", justify=CENTER, font=("Comic Sans MS", 16, "bold"))
        Input_P_cmb_search.place(x=20, y=10, width=200)
        Input_P_cmb_search.current(0)
        Input_P_search = ttk.Entry(
            Search_Member_Inner_Frame, textvariable=self.P_Search, font=("Comic Sans MS", 17, "bold"))
        Input_P_search.place(x=240, y=10)
        Input_P_search.focus()
        Input_P_search.bind("<Return>", lambda funct1: Member_Search_Btn())
        btn_P_Search = Button(Search_Member_Inner_Frame, command=Member_Search_Btn, text="Search", cursor="hand2", font=(
            "Comic Sans MS", 18, "bold"), bg="#000716", fg="white").place(x=540, y=10, width=180, height=35)
        btn_P_Clear = Button(Search_Member_Inner_Frame, command=Member_Clear_Btn, text="Clear", cursor="hand2", font=(
            "Comic Sans MS", 18, "bold"), bg="#000716", fg="white").place(x=740, y=10, width=180, height=35)

        Member_Frame = Frame(top, bd=10, relief=RIDGE, padx=10)
        Member_Table_Frame = Frame(
            Member_Frame, bd=10, relief=RIDGE, padx=0, pady=5)

        Member_Frame.place(x=0, y=135, height=465, relwidth=1)
        Member_Table_Frame.place(x=0, y=10, height=425, relwidth=1)

        Member_Xscroll = Scrollbar(Member_Table_Frame, orient=HORIZONTAL)
        Member_Yscroll = Scrollbar(Member_Table_Frame, orient=VERTICAL)

        self.Member_table = ttk.Treeview(Member_Table_Frame, column=("m_typ", "m_id", "fname", "lname", "add", "dpt", "gid",
                                          "mno", "amn","pw"), xscrollcommand=Member_Xscroll.set, yscrollcommand=Member_Yscroll.set)

        Member_Xscroll.pack(side=BOTTOM, fill=X)
        Member_Yscroll.pack(side=RIGHT, fill=Y)

        Member_Xscroll.config(command=self.Member_table.xview)
        Member_Yscroll.config(command=self.Member_table.yview)

        self.Member_table.heading("m_typ", text="Member Type")
        self.Member_table.heading("m_id", text="MemberId")
        self.Member_table.heading("fname", text="First Name")
        self.Member_table.heading("gid", text="Mail Id")
        self.Member_table.heading("mno", text="Mobile No")
        self.Member_table.heading("amn", text="Amount")
        self.Member_table.heading("lname", text="Last Name")
        self.Member_table.heading("add", text="Address")
        self.Member_table.heading("dpt", text="Department")
        self.Member_table.heading("amn", text="Current Amount")
        self.Member_table.heading("pw", text="Password")
        self.Member_table["show"] = "headings"
        self.Member_table.pack(fill=BOTH, expand=1)

        self.Member_table.column("m_typ", width=100, stretch=0, anchor=CENTER)
        self.Member_table.column("m_id", width=150, stretch=0, anchor=CENTER)
        self.Member_table.column("fname", width=200, stretch=0, anchor=CENTER)
        self.Member_table.column(
            "gid", width=200, stretch=0, anchor=CENTER)
        self.Member_table.column(
            "mno", width=150, stretch=0, anchor=CENTER)
        self.Member_table.column("amn", width=00, stretch=0, anchor=CENTER)
        self.Member_table.column("lname", width=150, stretch=0, anchor=CENTER)
        self.Member_table.column("add", width=200, stretch=0, anchor=CENTER)
        self.Member_table.column("dpt", width=200, stretch=0, anchor=CENTER)
        self.Member_table.column("amn", width=100, stretch=0, anchor=CENTER)
        self.Member_table.column("pw", width=150, stretch=0, anchor=CENTER)

        Member_Display_Data()
