##------------ ALL IMPORTED LIBRARY -----------------##

from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import time
import smtplib,ssl
import webbrowser

##------- Custom Library ---------##
from Book_Record import Book_Record_Class
from About import About_Class
from Help import Help_Class

##---------------- MAIN CLASS FOR USER PANEL / USER DASHBOARD ----------------##

class User_Panel_Class:
    
    ##------------- PARAMETERIZED CONSTRUCTOR WITH 3 PARAMETERS --------------##

    def __init__(self, root, User_Id):

        # root is the object of tk class.
        # username contain the user_name of the database enterd by the user in the login page.
        # dbpassword contain the password of the database enterd by the user in the login page.

        ## --------------------- Function For Manu Bar ----------------------- ##

        #---- Function for Minimize Window -----#

        def Do_Min(event=""):
            self.root.wm_state("iconic")

        
        def Book_Record_btn_f(event=""):
            User_Clear_Btn()
            Book_Record_obj = Book_Record_Class(username, dbpassword)
        
        def About_btn_f(event=""):
            User_Clear_Btn()
            About_obj = About_Class()
        
## --------------------- Function For Title Bar ----------------------- ##

        #---- Function For Changing Time ----#

        def tick():
            global time1
            time2 = time.strftime('%I:%M:%S %p')
            clock.config(text=time2)
            clock.after(200, tick)


#--------------- Function For Search Button -------------------#
        def User_Search_Btn(event=""):
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()
            cur.execute("select s.sr_no,i.ref_no,i.book_id,i.book_name,i.book_ed,b.book_sub,b.author,i.issue_date,i.due_date,i.return_date from issue_book as i,member_details as m,serial as s,books_details as b where i.member_id=m.member_id and s.ref_no=i.ref_no and i.book_name=b.book_name and m.member_id='" + self.ID+"'order by s.sr_no desc;")

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
    
            cur.execute(
                "select * from member_details where member_id=%s;", (self.ID))
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
            


## --------------------- Function For Info Frame Right ----------------------- ##

        #--- Display Book Function to Display All the Avalable Book In the Book List ----#

        def Display_Book(event=""):
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            cur.execute(
                "select book_name from books_details where rem_book > 0 order by book_name;")  
            result = cur.fetchall()

            if len(result) != 0:
                book_list.clear()
                for row in result:
                    book_list.append(str(row)[2:len(str(row))-3])
                    sqlCon.commit()
            else:
                book_list.clear()

            cur.execute(
                "select DISTINCT book_sub from books_details order by book_sub;") 
            result = cur.fetchall()

            if len(result) != 0:
                bsub.clear()
                for row in result:
                    bsub.append(str(row)[2:len(str(row))-3])
                    sqlCon.commit()
                sqlCon.close()
            else:
                sqlCon.close()
                bsub.clear()

        

        #----- Functions For Searching Books ------#

        def Update(data):
            book_ListBox.delete(0, END)
            for item in data:
                book_ListBox.insert(END, item)

        def Scankey(event):
            val = event.widget.get()
            if val == '':
                data = book_list
            else:
                data = []
                for item in book_list:
                    if val.lower() in item.lower():
                        data.append(item)
            Update(data)

        
        #---- Clear Data Button Function For Dashboard ----#
        def User_Clear_Btn(event=""):
            self.User_table.delete(*self.User_table.get_children())
            User_Search_Btn()
            self.entry.set("")
            self.cmbbsub.set("")
            self.newpw.set("")
            self.renewpw.set("")
            cmbox.delete(0, "end")
            Display_Book()
            Update(book_list)

        def Auto_Refresh(event=""):
            self.User_table.delete(*self.User_table.get_children())
            User_Search_Btn()
            if self.nob!=len(book_list) and self.cmbbsub.get()=="":
                self.nob=len(book_list)
                Display_Book()
                Update(book_list)
            self.User_table.after(2000,Auto_Refresh)
            
        def Change_Password_Btn(event=""):

            def SubmitBtn():
                if self.newpw.get()=="" or self.renewpw.get()=="":
                    messagebox.showerror('Library Management System', 'Please fill all the filds.', parent=top)
                    return
                elif self.newpw.get()!=self.renewpw.get():
                    messagebox.showerror('Library Management System', 'Do not Match Entered Passwowd.', parent=top)
                    return
                if self.newpw.get()==self.renewpw.get():
                    sqlCon = pymysql.connect(host="localhost", user=username, password=dbpassword, database="lms")
                    cur = sqlCon.cursor()
                    cur.execute("UPDATE member_details SET password=%s where member_id=%s;",(self.newpw.get(),self.ID))
                    sqlCon.commit()
                    sqlCon.close()
                    
                    try:
                        port = 587  # For SSL
                        host = "smtp-mail.outlook.com"
                        sender_email = "librarymanagementsystemproject@outlook.com"  # Enter your address
                        receiver_email = self.Mail.get() # Enter receiver address
                        password = "lms@1234"

                        subject="Changing Password"
                        body="Congratulations! You have been Change Your Password successfully. Now You Can Login With Your New Password Which You Set.\n\nMembership Information:\n\nMember ID: "+self.Member_ID.get()+"\nMember Type : "+self.Member_Type.get()+" \nFirst Name : "+self.First_Name.get()+" \nLast Name : "+self.Last_Name.get()+"\nMail ID : "+self.Mail.get()+" \nCurrent Amount : "+self.Cur_Amount.get()+" \n\nNew Password : "+self.newpw.get()+"\n\nIf You Don't Change Your Password Then Contact With Our Library Admin."
                        message = f'Subject: {subject}\n\n{body}'

                        server = smtplib.SMTP(host, port)
                        server.starttls()
                        server.login(sender_email, password)
                        output = server.sendmail(sender_email, receiver_email, message)

                    except:
                        pass

                    finally:
                        messagebox.showinfo(
                            'Library Management System', 'Password Change Successfully.', parent=top)
                        User_Clear_Btn()
                        


            top = Toplevel()
            
            top.grab_set()

            top.title("Library Management System | Change Password")

            app_width = 550
            app_height = 250

            screen_width = top.winfo_screenwidth()
            screen_height = top.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-13)}')
            top.resizable(False, False)
            top.iconbitmap('icon.ico')

            frame = Frame(top)
            frame.place(relheight=1, relwidth=1)

            
            Lbl_NewPs = Label(frame, text="New Password:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=20).grid(row=0, column=0, sticky=W)

            Input_NewPs = ttk.Entry(frame, font=(
                "Comic Sans MS", 16, "bold"), textvariable=self.newpw)
            Input_NewPs.grid(row=0, column=1, sticky=W)
            Input_NewPs.bind("<Return>", lambda funct1: Input_ReNew.focus())
            Input_NewPs.focus()

            Lbl_ReNew = Label(frame, text="Re-enter Password:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=15).grid(row=1, column=0, sticky=W)

            Input_ReNew = ttk.Entry(frame, font=(
                "Comic Sans MS", 16, "bold"), textvariable=self.renewpw)
            Input_ReNew.grid(row=1, column=1, sticky=W)

            Btn_Return_Book = Button(frame, text="Submit", width=15, bg="#000716", cursor="hand2", fg="white", font=(
                "Comic Sans MS", 15, "bold"), command=SubmitBtn).place(x=180, y=160)

        
        #------ Function For Close Window -------#

        def Qt_Win(event=""):
            qt = messagebox.askokcancel(
                'Library Management System', 'Are you sure you want to Quit?')
            if qt:
                self.root.destroy()
            else:
                pass

        def Help_btn_f(event=""):
            User_Clear_Btn()
            Help_obj = Help_Class()

        def open_browser():
            qt = messagebox.askokcancel(
                'Library Management System', 'This Window Will Be Close.\nYou Wiil Be Redirect To Our E-Library Page.')
            if qt:
                self.root.destroy()
                webbrowser.open_new("https://spclms.blogspot.com/")
            else:
                pass


## --------------------- Function For Data Frame ----------------------- ##

        #---- Display Data Function to Display All record on the dashboard in form of Table ----#


        #---- --- ----#

        def check_input(event):
                value = event.widget.get()

                if value == '':
                    cmbox['values'] = bsub
                    Display_Book()
                    Update(book_list)
                else:
                    data = []
                    for item in bsub:
                        if value.lower() in item.lower():
                            data.append(item)

                    cmbox['values'] = data


        def celectbysubject(event=""):
            self.entry.set("")
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            cur.execute(
                "select book_name from books_details where rem_book > 0 and book_sub =%s order by book_name;", (self.cmbbsub.get()))  
            result = cur.fetchall()

            if len(result) != 0:
                book_list.clear()
                for row in result:
                    book_list.append(str(row)[2:len(str(row))-3])
                    sqlCon.commit()
            else:
                book_list.clear()
            sqlCon.close()
            Update(book_list)
            

        

## --------------------------- Instance Valiable ------------------- ##

        self.root = root
        self.root.focus_force()
        self.ID=User_Id
        self.newpw=StringVar()
        self.renewpw=StringVar()

        username="user"
        dbpassword="1234"
        
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
        self.nob=0
        self.cmbbsub=StringVar()

        self.entry = StringVar()
        book_list = []
        bsub=[]



## -------------------- Dash Board Window Size --------------------- ##

        self.root.title("Library Management System")  # Title of the app
        self.root.attributes('-fullscreen', True)
        ht = self.root.winfo_screenheight()  # Height of the Window
        wt = self.root.winfo_screenwidth()  # Width of the Window
        # Setting geometry of main screen
        self.root.geometry("%dx%d+%d+%d" % (wt, ht, 0, 0))


## ----------------------- Menu Bar ------------------ ##

        menubar = Menu(self.root)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(
            label="Minimize", command=Do_Min, accelerator="F11")
        self.root.bind("<F11>", Do_Min)
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit", command=Qt_Win, accelerator="Ctrl+Q")
        self.root.bind("<Control_L><q>", Qt_Win)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(
            label="Refresh", accelerator="Esc", command=User_Clear_Btn)
        self.root.bind("<Escape>", User_Clear_Btn)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        show_menu = Menu(menubar, tearoff=0)
        show_menu.add_command(label="All Books Record",
                              command=Book_Record_btn_f)
        menubar.add_cascade(label="Show", menu=show_menu)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Help", accelerator="F1",command=Help_btn_f)
        self.root.bind("<F1>", Help_btn_f)
        help_menu.add_command(
            label="About", command=About_btn_f)
        menubar.add_cascade(label="Help", menu=help_menu)


        self.root.config(menu=menubar)


## --------------------- Title Bar ------------------ ##

        Title = Label(self.root, text="Library Management System", fg="#000716", bd=15, relief=RIDGE,
                      font=("Comic Sans MS", 30, "bold"), padx=2, pady=6)
        Title.pack(side=TOP, fill=X)

        clock = Label(Title, fg="#000716", bd=10, relief=FLAT,
                      font=("Comic Sans MS", 20, "bold"), padx=2, pady=6)
        clock.pack(side=RIGHT, expand=0)
        date = Label(Title, fg="#000716", bd=10, relief=FLAT,
                     font=("Comic Sans MS", 20, "bold"), padx=2, pady=6)
        date.pack(side=LEFT, expand=0)

        date.config(text=time.strftime('%d %B %Y'))

        tick()


## ---------------- Frame Setting For Info_Frame ----------------- ##

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20)
        if wt > 1400:
            frame.place(x=0, y=110, width=wt, height=420)
        else:
            frame.place(x=0, y=110, width=wt, height=380)


# ------------------------------ Info_Frame_Left --------------------------#

        Info_Frame_Left = LabelFrame(frame, text="Library Membership Information", fg="#000716", bd=10, relief=RIDGE,
                                     font=("Comic Sans MS", 14, "bold"))
        # Screen Size Adjustment
        if wt > 1400:
            Info_Frame_Left.place(x=0, y=5, width=wt *
                                  (2 / 3) - 120, height=380)
            fsize = 17
            lfsize=14
            wd=20
            py=7
            fheight=235
            cmbwidth=200
            ad=0

        else:
            Info_Frame_Left.place(x=0, y=5, width=wt *
                                  (2 / 3) - 120, height=345)
            fsize = 15
            wd=20
            lfsize=12
            py=6
            fheight=205
            cmbwidth=150
            ad=110
        # ------- Label and Input Field for Left side of the Info_Frame_Left ------- #

        UR_Inner_Frame = Frame(Info_Frame_Left, bd=10, relief=RIDGE, padx=0)

        UR_Inner_Frame.place(x=15, y=5, height=fheight, relwidth=.97)
        
        Lbl_Member_Type = Label(UR_Inner_Frame, text="Member Type:", font=(
            "Comic Sans MS", lfsize-1, "bold"), padx=20, pady=py).grid(row=0, column=0, sticky=W)
        Input_Member_Type = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", lfsize, "bold"), width=wd, textvariable=self.Member_Type).grid(row=0, column=1, sticky=W)

        Lbl_Member_ID = Label(UR_Inner_Frame, text="Member ID:", font=(
            "Comic Sans MS", lfsize-1, "bold"), padx=20, pady=py).grid(row=1, column=0, sticky=W)
        Input_Member_ID = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", lfsize, "bold"), width=wd, textvariable=self.Member_ID)
        Input_Member_ID.grid(row=1, column=1, sticky=W)

        Lbl_First_Name = Label(UR_Inner_Frame, text="First Name:", font=(
            "Comic Sans MS", lfsize-1, "bold"), padx=20, pady=py).grid(row=2, column=0, sticky=W)
        Input_First_Name = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", lfsize, "bold"), width=wd, textvariable=self.First_Name).grid(row=2, column=1, sticky=W)

        Lbl_Last_Name = Label(UR_Inner_Frame, text="Last Name:", font=(
            "Comic Sans MS", lfsize-1, "bold"), padx=20, pady=py).grid(row=3, column=0, sticky=W)
        Input_Last_Name = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", lfsize, "bold"), width=wd, textvariable=self.Last_Name).grid(row=3, column=1, sticky=W)

        Lbl_Address = Label(UR_Inner_Frame, text="Address:", font=(
            "Comic Sans MS", lfsize-1, "bold"), padx=20, pady=py).grid(row=4, column=0, sticky=W)
        Input_Address = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", lfsize, "bold"), width=wd, textvariable=self.Address).grid(row=4, column=1, sticky=W)

        Lbl_Department = Label(UR_Inner_Frame, text="Department:", font=(
            "Comic Sans MS", lfsize-1, "bold"), padx=20, pady=py).grid(row=0, column=2, sticky=W)
        Input_Department = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", lfsize, "bold"), width=wd, textvariable=self.Department).grid(row=0, column=3, sticky=W)

        Lbl_Mail = Label(UR_Inner_Frame, text="Mail ID:", font=(
            "Comic Sans MS", lfsize-1, "bold"), padx=20, pady=py).grid(row=1, column=2, sticky=W)
        Input_Mail = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", lfsize, "bold"), width=wd, textvariable=self.Mail).grid(row=1, column=3, sticky=W)

        Lbl_PH = Label(UR_Inner_Frame, text="Mobile Number:", font=(
            "Comic Sans MS", lfsize-1, "bold"), padx=20, pady=py).grid(row=2, column=2, sticky=W)
        Input_PH = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", lfsize, "bold"), width=wd, textvariable=self.Ph).grid(row=2, column=3, sticky=W)

        Lbl_Cur_Amount = Label(UR_Inner_Frame, text="Balance:", font=(
            "Comic Sans MS", lfsize-1, "bold"), padx=20, pady=py).grid(row=3, column=2, sticky=W)
        Input_Cur_Amount = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", lfsize, "bold"), width=wd, textvariable=self.Cur_Amount).grid(row=3, column=3, sticky=W)
        Lbl_B_Count = Label(UR_Inner_Frame, text="Book Count:", font=(
            "Comic Sans MS", lfsize-1, "bold"), padx=20, pady=py).grid(row=4, column=2, sticky=W)
        Input_B_Count = ttk.Entry(UR_Inner_Frame, state="readonly", font=(
            "Comic Sans MS", lfsize, "bold"), width=wd, textvariable=self.B_Count).grid(row=4, column=3, sticky=W)
        
        if wt > 1400:
            Search_User_Inner_Frame = Frame(Info_Frame_Left, bd=10, relief=RIDGE,pady=5,padx=5)
            Search_User_Inner_Frame.place(x=15, y=245, height=85, relwidth=.97)
        else:
            Search_User_Inner_Frame = Frame(Info_Frame_Left, bd=10, relief=RIDGE,pady=5,padx=7)
            Search_User_Inner_Frame.place(x=15, y=220, height=80, relwidth=.97)

        Btn_Clear = Button(Search_User_Inner_Frame,command=User_Clear_Btn, text="Refresh", font=("Comic Sans MS", fsize, "bold"), cursor="hand2", width=14, bg="#000716",
                              fg="white").grid(row=0, column=0)
        Btn_Online = Button(Search_User_Inner_Frame, text="E-Books", command=open_browser,font=("Comic Sans MS", fsize, "bold"), cursor="hand2", width=14, bg="#000716",
                              fg="white").grid(row=0, column=1)                      
        Btn_Change_PW = Button(Search_User_Inner_Frame,command=Change_Password_Btn, text="Change Password", font=("Comic Sans MS", fsize, "bold"), cursor="hand2", width=15, bg="#000716",
                                 fg="white").grid(row=0, column=2)
        Btn_Exit_Data = Button(Search_User_Inner_Frame, command=Qt_Win, text="Exit", font=("Comic Sans MS", fsize, "bold"), cursor="hand2", width=13,
                               bg="#000716", fg="white").grid(row=0, column=3)


## --------------------------------------- Info_Frame_Right -------------------------- ##

        Info_Frame_Right = LabelFrame(frame, text="Book Details", fg="#000716", bd=10, relief=RIDGE,
                                      font=("Comic Sans MS", 14, "bold"))
        #Info_Frame_Right_Right = LabelFrame(frame, relief=FLAT)

        # Screen Size Adjustment
        if wt > 1400:
            Info_Frame_Right.place(x=wt * (2 / 3) - 105,
                                   y=5, width=wt * 1 / 3 + 45, height=380)
            lbh = 0.8
            lw=0.57
            cbw=0.33
        else:
            Info_Frame_Right.place(x=wt * (2 / 3) - 105,
                                   y=5, width=wt * 1 / 3 + 45, height=345)
            
            lbh = 0.75
            lw=0.53
            cbw=0.37

        book_ScrollbarY = Scrollbar(Info_Frame_Right)
        book_ScrollbarY.pack(side=RIGHT, fill=Y)

        book_ScrollbarX = Scrollbar(Info_Frame_Right, orient=HORIZONTAL)
        book_ScrollbarX.pack(side=BOTTOM, fill=X)

        book_ListBox = Listbox(Info_Frame_Right, yscrollcommand=book_ScrollbarY.set,
                               xscrollcommand=book_ScrollbarX.set, font=("Comic Sans MS", 14, "bold"), cursor="hand2", bd=2)
        book_ListBox.place(x=10,y=50,relwidth=0.93,relheight=lbh)

        book_ScrollbarY.config(command=book_ListBox.yview)
        book_ScrollbarX.config(command=book_ListBox.xview)

        # display books name in book list box
        Display_Book()
        self.nob=len(book_list)
    
        
        #---------cmb--********-#

        cmbox=ttk.Combobox(Info_Frame_Right, font=(
            "Comic Sans MS", 18, "bold"),textvariable=self.cmbbsub)
        cmbox.place(x=10,y=5,relwidth=cbw)
        cmbox['values'] = bsub
        cmbox.bind('<KeyRelease>', check_input)
        cmbox.bind('<<ComboboxSelected>>', celectbysubject)
        # Search Book Input
        entry = ttk.Entry(Info_Frame_Right, font=(
            "Comic Sans MS", 18, "bold"), textvariable=self.entry)
        entry.place(x=200,y=5,relwidth=lw)
        entry.bind('<KeyRelease>', Scankey)
        Update(book_list)


## ----------------------------------Database Frame & Table Frame --------------------------------- ##

        DatabaseFrame = Frame(self.root, bd=10, relief=RIDGE, padx=10)
        Table_Frame = Frame(DatabaseFrame, bd=6, relief=RIDGE, padx=0, pady=0)
        if wt > 1400:
            DatabaseFrame.place(x=0, y=540, width=wt, height=275)
            Table_Frame.place(x=0, y=10, width=wt-40, height=235)
        else:
            DatabaseFrame.place(x=0, y=500, relwidth=1, height=220)
            Table_Frame.place(x=0, y=10, width=wt-40, height=180)

        Xscroll = Scrollbar(Table_Frame, orient=HORIZONTAL)
        Yscroll = Scrollbar(Table_Frame, orient=VERTICAL)

        self.User_table = ttk.Treeview(Table_Frame, column=("sr_no", "refno", "bid", "bname", "bed", "bsub",
                                       "bauth", "bissu", "bdue", "bret"), xscrollcommand=Xscroll.set, yscrollcommand=Yscroll.set)

        Xscroll.pack(side=BOTTOM, fill=X)
        Yscroll.pack(side=RIGHT, fill=Y)

        Xscroll.config(command=self.User_table.xview)
        Yscroll.config(command=self.User_table.yview)

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
        self.User_table.column("bname", width=300, stretch=0, anchor=CENTER)
        self.User_table.column("bed", width=100, stretch=0, anchor=CENTER)
        self.User_table.column("bsub", width=170, stretch=0, anchor=CENTER)
        self.User_table.column("bauth", width=200, stretch=0, anchor=CENTER)
        self.User_table.column("bissu", width=100, stretch=0, anchor=CENTER)
        self.User_table.column("bdue", width=100, stretch=0, anchor=CENTER)
        self.User_table.column("bret", width=100, stretch=0, anchor=CENTER)

        self.User_table["show"] = "headings"
        self.User_table.pack(fill=BOTH, expand=1)


        Lbl_footer = Label(self.root,text="Developed By Department of Computer Science, Syamaprasad College.",font=("Comic Sans MS", 13, "bold"),bg="#000716",fg="#f1f1f1")
        if wt > 1400:
             Lbl_footer.place(x=0,y=815,relwidth=1,height=30)
        else:
            Lbl_footer.place(x=0,y=720,relwidth=1,height=30)


        User_Search_Btn()
        Auto_Refresh()

## -------------------------------- TTK Customization ---------------------------------- ##
        style1 = ttk.Style()
        style1.configure('TEntry', background='black')
        style1.configure('TSpinbox', background='black',
                         selectbackground='none', selectforeground='black')
        style1.configure('TCombobox', background='black')
        style1.configure('Treeview', font=("Comic Sans MS", 10))
        style1.configure('Treeview.Heading', font=("Comic Sans MS", 10,"bold"))
