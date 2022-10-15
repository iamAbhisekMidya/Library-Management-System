from faulthandler import disable
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import pymysql

class Data_Entry_Class:

    def __init__(self, username, dbpassword):        


        def Display_Data(*args):
            dt=self.Pcmbox.get()
            x=dt[6:10]+"-"+dt[3:5]+"-"+dt[0:2]
            
            if(x=="--"):
                return
            
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            cur.execute("select s.sr_no,i.ref_no,m.member_id,i.book_id,i.book_name,i.book_ed,i.issue_date,i.due_date,i.return_date from issue_book as i,member_details as m,serial as s where i.member_id=m.member_id and s.ref_no=i.ref_no and i.return_date='"+x+"' order by s.sr_no desc;")
            result = cur.fetchall()

            if len(result) != 0:
                self.Return_Table.delete(*self.Return_Table.get_children())

                for row in result:
                    self.Return_Table.insert('', END, values=row)

                sqlCon.commit()
                sqlCon.close()
            else:
                sqlCon.close()
                self.Return_Table.delete(*self.Return_Table.get_children())
                
            sqlCon = pymysql.connect(host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            cur.execute("select s.sr_no,i.ref_no,m.member_id,i.book_id,i.book_name,i.book_ed,i.issue_date,i.due_date from issue_book as i,member_details as m,serial as s where i.member_id=m.member_id and s.ref_no=i.ref_no and i.issue_date='"+x+"' order by s.sr_no desc;")
            result = cur.fetchall()

            if len(result) != 0:
                self.Issued_Table.delete(*self.Issued_Table.get_children())

                for row in result:
                    self.Issued_Table.insert('', END, values=row)

                sqlCon.commit()
                sqlCon.close()
            else:
                sqlCon.close()
                self.Issued_Table.delete(*self.Issued_Table.get_children())

                
           
        self.Pcmbox = StringVar()
        
        top = Toplevel()
        top.grab_set()
        top.focus_force()

        top.title("Library Management System | Perticular Day Record")

        app_width = 900
        app_height = 580
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-13)}')
        top.resizable(False, False)
        top.iconbitmap('icon.ico')

        Frame1 = Frame(top, bd=10, relief=RIDGE)
        Frame1.place(x=0, y=5, relwidth=1, height=75)

        cal = DateEntry(Frame1,date_pattern='dd-mm-yyyy',state="readonly",borderwidth=5,textvariable=self.Pcmbox, cursor="hand2",justify=CENTER,font=("Comic Sans MS", 14, "bold"))
        cal.place(x=10, y=10, relwidth=0.98,height=40)     
        self.Pcmbox.trace('w',Display_Data)
        

        Frame2 = Frame(top, bd=10, relief=RIDGE)
        Frame2.place(x=0, y=90, relwidth=1, height=245)

        Frame2Inner = LabelFrame(Frame2, text="Returned Book", fg="#000716", bd=10, relief=RIDGE,
                                                font=("Comic Sans MS", 10, "bold"))
        
        Frame2Inner.place(x=15, y=5, height=210, relwidth=.97)
        Return_Table_Xscroll = Scrollbar(Frame2Inner, orient=HORIZONTAL)
        Return_Table_Yscroll = Scrollbar(Frame2Inner, orient=VERTICAL)

        self.Return_Table = ttk.Treeview(Frame2Inner, column=("sr_no", "refno", "mid", "bid", "bname", "bed", "bissu", "bdue","ret"), xscrollcommand=Return_Table_Xscroll.set, yscrollcommand=Return_Table_Yscroll.set)

        Return_Table_Xscroll.pack(side=BOTTOM, fill=X)
        Return_Table_Yscroll.pack(side=RIGHT, fill=Y)

        Return_Table_Xscroll.config(command=self.Return_Table.xview)
        Return_Table_Yscroll.config(command=self.Return_Table.yview)

        self.Return_Table.heading("sr_no", text="Serial No")
        self.Return_Table.heading("refno", text="Reference No")
        self.Return_Table.heading("mid", text="Member Id")
        self.Return_Table.heading("bid", text="Book Id")
        self.Return_Table.heading("bname", text="Book Name")
        self.Return_Table.heading("bed", text="Book Edition")
        self.Return_Table.heading("bissu", text="Issue Date")
        self.Return_Table.heading("bdue", text="Due Date")
        self.Return_Table.heading("ret", text="Returned Date")
        self.Return_Table["show"] = "headings"
        self.Return_Table.pack(fill=BOTH, expand=1)

        self.Return_Table.column("sr_no", width=100, stretch=0, anchor=CENTER)
        self.Return_Table.column("refno", width=150, stretch=0, anchor=CENTER)
        self.Return_Table.column("mid", width=150, stretch=0, anchor=CENTER)
        self.Return_Table.column("bid", width=150, stretch=0, anchor=CENTER)
        self.Return_Table.column("bname", width=200, stretch=0, anchor=CENTER)
        self.Return_Table.column("bed", width=100, stretch=0, anchor=CENTER)
        self.Return_Table.column("bissu", width=100, stretch=0, anchor=CENTER)
        self.Return_Table.column("bdue", width=100, stretch=0, anchor=CENTER)
        self.Return_Table.column("ret", width=100, stretch=0, anchor=CENTER)

       
        Frame3 = Frame(top, bd=10, relief=RIDGE, padx=10)
        Frame3.place(x=0, y=345, height=235, relwidth=1)
        
        Frame3Inner = LabelFrame(Frame3, bd=10,text='Issued Book',fg="#000716",  relief=RIDGE,font=("Comic Sans MS", 10, "bold"))
        Frame3Inner.place(x=0, y=10, height=190, relwidth=1)

        Issued_Xscroll = Scrollbar(Frame3Inner, orient=HORIZONTAL)
        Issued_Yscroll = Scrollbar(Frame3Inner, orient=VERTICAL)

        self.Issued_Table = ttk.Treeview(Frame3Inner, column=("sr_no", "refno", "mid", "bid", "bname", "bed", "bissu", "bdue"), xscrollcommand=Issued_Xscroll.set, yscrollcommand=Issued_Yscroll.set)

        Issued_Xscroll.pack(side=BOTTOM, fill=X)
        Issued_Yscroll.pack(side=RIGHT, fill=Y)

        Issued_Xscroll.config(command=self.Issued_Table.xview)
        Issued_Yscroll.config(command=self.Issued_Table.yview)

        self.Issued_Table.heading("sr_no", text="Serial No")
        self.Issued_Table.heading("refno", text="Reference No")
        self.Issued_Table.heading("mid", text="Member Id")
        self.Issued_Table.heading("bid", text="Book Id")
        self.Issued_Table.heading("bname", text="Book Name")
        self.Issued_Table.heading("bed", text="Book Edition")
        self.Issued_Table.heading("bissu", text="Issue Date")
        self.Issued_Table.heading("bdue", text="Due Date")
        self.Issued_Table["show"] = "headings"
        self.Issued_Table.pack(fill=BOTH, expand=1)

        self.Issued_Table.column("sr_no", width=100, stretch=0, anchor=CENTER)
        self.Issued_Table.column("refno", width=150, stretch=0, anchor=CENTER)
        self.Issued_Table.column("mid", width=150, stretch=0, anchor=CENTER)
        self.Issued_Table.column("bid", width=150, stretch=0, anchor=CENTER)
        self.Issued_Table.column("bname", width=200, stretch=0, anchor=CENTER)
        self.Issued_Table.column("bed", width=100, stretch=0, anchor=CENTER)
        self.Issued_Table.column("bissu", width=100, stretch=0, anchor=CENTER)
        self.Issued_Table.column("bdue", width=100, stretch=0, anchor=CENTER)

        Display_Data()