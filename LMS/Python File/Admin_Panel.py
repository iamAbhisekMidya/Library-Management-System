##------------ ALL IMPORTED LIBRARY -----------------##
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import pymysql
import time
import datetime
import os
import shutil
import smtplib,ssl
import babel.numbers
from pymysql import NULL

##------- Custom Library ---------##

from Add_Member import Add_Member_Class
from Not_Returned_Book import Not_Returned_Book_Class
from Particular_User_Record import Particular_User_Record_Class
from Member_Record import Member_Record_Class
from Book_Record import Book_Record_Class
from Data_Entry import Data_Entry_Class
from About import About_Class
from Lost_Book import Lost_Book_Class
from Help import Help_Class

##---------------- MAIN CLASS FOR ADMIN PANEL / ADMIN DASHBOARD ----------------##


class Admin_Panel_Class:

    ##------------- PARAMETERIZED CONSTRUCTOR WITH 3 PARAMETERS --------------##

    def __init__(self, root, username, dbpassword):

        # root is the object of tk class.
        # username contain the user_name of the database enterd by the user in the login page.
        # dbpassword contain the password of the database enterd by the user in the login page.

        ## --------------------- Function For Manu Bar ----------------------- ##

        #---- Function for Minimize Window -----#

        def Do_Min(event=""):
            self.root.wm_state("iconic")

        #--- Modify Member Button Function ---#

        def Mod_Member_btn_f(event=""):

            #---- Function for Modify Member Autofill -----#

            def Autofill_Modify_Member(event=""):
                try:
                    if(len(event.widget.get())) >= 4:
                        try:
                            sqlCon = pymysql.connect(
                                host="localhost", user=username, password=dbpassword, database="lms")
                            cur = sqlCon.cursor()

                            cur.execute(
                                "select member_type,first_name,last_name,address,dept,mobile,mail from member_details where member_id=%s;", (event.widget.get()))
                            result = cur.fetchall()

                            if len(result) != 0:
                                for row in result:
                                    self.M_Type.set(row[0])
                                    self.F_Name.set(row[1])
                                    self.L_Name.set(row[2])
                                    self.Add.set(row[3])
                                    lst=row[4].split()
                                    st=""
                                    for i in range(1,len(lst)):
                                        st=st+lst[i]+" "

                                    self.St.set(lst[0])
                                    Deptselect()
                                    self.Dt.set(st.strip())
                                    self.Phone.set(row[5])
                                    self.Ml.set(row[6])
                                    self.val=1
                            else:
                                self.M_Type.set("")
                                self.F_Name.set("")
                                self.L_Name.set("")
                                self.Add.set("")
                                self.Dt.set("")
                                self.Phone.set("")
                                self.Ml.set("")
                                self.St.set("")
                                self.val=0

                            sqlCon.close()

                        except:
                            pass
                    else:
                        self.M_Type.set("")
                        self.F_Name.set("")
                        self.L_Name.set("")
                        self.Add.set("")
                        self.Dt.set("")
                        self.Phone.set("")
                        self.Ml.set("")
                        self.St.set("")
                        self.val=0
                except:
                    pass

            #---- Function for Modify Member Submit Button -----#

            def Btn_Mod_M():

                if self.M_Type.get() == "" or self.F_Name.get() == "" or self.L_Name.get() == "" or self.Add.get() == "" or self.St.get()=="" or self.Dt.get()  == "" or self.C_Amount.get() == "" or self.Phone.get() == "":
                    messagebox.showerror(
                        'Library Management System', 'Please Fill All The Fields.', parent=top)
                    return
                elif self.val==0:
                    messagebox.showerror(
                        'Library Management System', 'Member Id not found.', parent=top)
                    return

                if self.F_Name.get().replace(' ','').isalpha():
                    if self.L_Name.get().replace(' ','').isalpha():
                        if self.C_Amount.get().isnumeric() and int(self.C_Amount.get()) >=0 and int(self.C_Amount.get())<=25000:
                            if self.Phone.get().isnumeric():
                                if len(self.Phone.get())==10:
                                    try:
                                        sqlCon = pymysql.connect(
                                            host="localhost", user=username, password=dbpassword, database="lms")
                                        cur = sqlCon.cursor()

                                        cur.execute("update member_details set member_type=%s,first_name=%s,last_name=%s,address=%s,dept=%s,mobile=%s,amount=amount+%s where member_id=%s;", (self.M_Type.get(
                                        ).title(), self.F_Name.get().title(), self.L_Name.get().title(), self.Add.get().title(), self.St.get()+" "+self.Dt.get(), self.Phone.get(), self.C_Amount.get(), self.M_Id.get()))

                                        sqlCon.commit()
                                        sqlCon.close()

                                        sqlCon = pymysql.connect(
                                            host="localhost", user=username, password=dbpassword, database="lms")
                                        cur = sqlCon.cursor()

                                        cur.execute("select amount from member_details where member_id=%s",(self.M_Id.get()))
                                        result = cur.fetchall()
                                        if len(result) != 0:
                                            for row in result:
                                                val=row[0]

                                        sqlCon.close()
                                                                                    
                                        try:
                                            Phone=self.Phone.get()
                                            Phone=Phone[0:3]+"XXXX"+Phone[7:10]
                                            port = 587  # For SSL
                                            host = "smtp-mail.outlook.com"
                                            sender_email = "librarymanagementsystemproject@outlook.com"  # Enter your address
                                            receiver_email = self.Ml.get() # Enter receiver address
                                            password = "lms@1234"

                                            subject="Update Member Details"
                                            body="Updation Of Member Details Successfully on Our Library Management System.\n\nMembership Information:\n\nYour Member Id/Username is : "+self.M_Id.get()+" \nMember Type : "+self.M_Type.get().title()+" \nFirst Name : "+self.F_Name.get().title()+" \nLast Name : "+self.L_Name.get().title()+" \nAddress : "+self.Add.get().title()+" \nDepartment : "+self.St.get()+" "+self.Dt.get()+"\nMail ID : "+self.Ml.get()+" \nMobile No : "+Phone+" \nAdd Amount : "+self.C_Amount.get()+"\nCurrent Amount : "+str(val)+"\n\nContact Admin Of Our Library For Any Information."
                                            

                                            message = f'Subject: {subject}\n\n{body}'

                                            server = smtplib.SMTP(host, port)
                                            server.starttls()
                                            server.login(sender_email, password)
                                            output = server.sendmail(sender_email, receiver_email, message)

                                        except:
                                            pass
                                        finally:
                                            messagebox.showinfo('Library Management System', 'Member ' +
                                                                self.M_Id.get()+' Update Successfully.', parent=top)
                                            Clear_Data()
                                            self.M_Id.set("")
                                    except:
                                        sqlCon.close()
                                        messagebox.showerror(
                                            'Library Management System', 'Phone Number Already Exist.\nPlease check again.', parent=top)

                                else:
                                    messagebox.showerror(
                                    'Library Management System', 'Length of Phone Numbers Must be 10', parent=top)
                            else:
                                messagebox.showerror(
                                    'Library Management System', 'Phone Number Do not Contain Any Charecter Or Special Charecter', parent=top)

                        else:
                            messagebox.showerror(
                                'Library Management System', 'Deposit Amount Do not Contain Any Charecters Or Special Charecters.\n\t\tAnd\n\n0 >= Deposite Amount <= 25,000', parent=top)

                    else:
                        messagebox.showerror(
                            'Library Management System', 'Last Name Do not Contain Any Numbers Or Special Charecter', parent=top)

                else:
                    messagebox.showerror(
                        'Library Management System', 'First Name Do not Contain Any Numbers Or Special Charecter', parent=top)
        


            def Deptselect(event=""):
                self.Dt.set("")
                if self.St.get()=="B.Sc":
                    Input_Dept['value'] = ["Computer Science","Mathematics","Physics","Geography","Electronics","Economics","Biological Science","Others"]
                elif self.St.get()=="B.Com":
                    Input_Dept['value'] = ["Commerce","Others"]
                elif self.St.get()=="Other":
                    Input_Dept['value'] = ["Office Staff"]
                else:
                    Input_Dept['value'] = ["Bengali","English","French","Hindi","Philosophy","Education","History","Political Science","Sanskrit","Others"]



            top = Toplevel()
            top.grab_set()

            top.title("Library Management System | Modify Member")

            Clear_Data()
            self.val=0
            app_width = 800
            app_height = 600
            screen_width = top.winfo_screenwidth()
            screen_height = top.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-50)}')
            top.resizable(False, False)
            top.iconbitmap('icon.ico')
            frame = Frame(top)
            frame.place(relheight=1, relwidth=1)

            dmylbl = Label(frame, font=("Comic Sans MS", 8,
                           "bold")).grid(row=0, column=0)

            Lbl_Member_ID = Label(frame, text="Member ID:", font=(
                "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=1, column=0, sticky=W)

            Input_Member_ID = ttk.Entry(frame, width=21,font=(
                "Comic Sans MS", 20, "bold"), textvariable=self.M_Id)
            Input_Member_ID.grid(row=1, column=1, sticky=W)
            Input_Member_ID.focus()
            Input_Member_ID.bind('<KeyRelease>', Autofill_Modify_Member)
            Input_Member_ID.bind("<Return>", lambda funct1: Input_PH.focus())

            Lbl_PH = Label(frame, text="Mobile Number:", font=(
                "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=2, column=0, sticky=W)

            Input_PH = ttk.Entry(frame,width=21, font=(
                "Comic Sans MS", 20, "bold"), textvariable=self.Phone)
            Input_PH.grid(row=2, column=1, sticky=W)
            Input_PH.bind("<Return>", lambda funct1: Input_Member_Type.focus())

            Lbl_Member_Type = Label(frame, text="Member Type:", font=(
                "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=3, column=0, sticky=W)

            Input_Member_Type = ttk.Combobox(frame, font=(
                "Comic Sans MS", 20, "bold"), width=20, cursor="hand2", state="readonly", textvariable=self.M_Type)
            Input_Member_Type['value'] = ("Student", "Teacher","Staff")
            Input_Member_Type.grid(row=3, column=1, sticky=W)
            Input_Member_Type.bind(
                "<Return>", lambda funct1: Input_First_Name.focus())

            Lbl_First_Name = Label(frame, text="First Name:", font=(
                "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=4, column=0, sticky=W)

            Input_First_Name = ttk.Entry(frame,width=21, font=(
                "Comic Sans MS", 20, "bold"), textvariable=self.F_Name)
            Input_First_Name.grid(row=4, column=1, sticky=W)
            Input_First_Name.bind(
                "<Return>", lambda funct1: Input_Last_Name.focus())

            Lbl_Last_Name = Label(frame, text="Last Name:", font=(
                "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=5, column=0, sticky=W)

            Input_Last_Name = ttk.Entry(frame,width=21, font=(
                "Comic Sans MS", 20, "bold"), textvariable=self.L_Name)
            Input_Last_Name.grid(row=5, column=1, sticky=W)
            Input_Last_Name.bind(
                "<Return>", lambda funct1: Input_Address.focus())

            Lbl_Address = Label(frame, text="Address:", font=(
                "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=6, column=0, sticky=W)

            Input_Address = ttk.Entry(frame,width=21, font=(
                "Comic Sans MS", 20, "bold"), textvariable=self.Add)
            Input_Address.grid(row=6, column=1, sticky=W)
            Input_Address.bind("<Return>", lambda funct1: Input_St.focus())

            
            Lbl_Dept = Label(frame, text="Department:", font=(
            "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=7, column=0, sticky=W)

            Input_St = ttk.Combobox(frame, font=(
                "Comic Sans MS", 18, "bold"), width=5, cursor="hand2", state="readonly", textvariable=self.St)
            Input_St.grid(row=7, column=1, sticky=W)
            Input_St['value']=["B.Sc","B.Com","B.A","Other"]
            Input_St.bind('<<ComboboxSelected>>', Deptselect)
            Input_St.bind("<Return>", lambda funct1: Input_Dept.focus())

            Input_Dept = ttk.Combobox(frame, font=(
                "Comic Sans MS", 18, "bold"), width=14, cursor="hand2", state="readonly", textvariable=self.Dt)
            
            Input_Dept.grid(row=7, column=1, sticky=W,padx=110)
            Input_Dept.bind("<Return>", lambda funct1: Input_Add_Amount.focus())

            Lbl_Add_Amount = Label(frame, text="Add Amount:", font=(
                "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=8, column=0, sticky=W)

            Input_Add_Amount = ttk.Entry(frame, width=21,font=(
                "Comic Sans MS", 20, "bold"), textvariable=self.C_Amount)
            Input_Add_Amount.grid(row=8, column=1, sticky=W)

            Btn_Mod_Member = Button(frame, text="Update Member Details", width=20, bg="#000716", cursor="hand2",
                                    fg="white", font=("Comic Sans MS", 15, "bold"), command=Btn_Mod_M).place(x=300, y=530)

        #------ Delete data from database Function ---------#

        def delete_data(event=""):
            if len(self.Ref_no.get()) > 1:
                try:
                    dt = messagebox.askyesno(
                        'Library Management System', 'Are you sure you want to Delete Ref No : '+self.Ref_no.get()+' ?')
                    if dt:
                        sqlCon = pymysql.connect(
                            host="localhost", user=username, password=dbpassword, database="lms")
                        cur = sqlCon.cursor()

                        cur.execute(
                            "delete from pending where ref_no=%s", (self.Ref_no.get()))
                        cur.execute(
                            "delete from serial where ref_no=%s", (self.Ref_no.get()))

                        cur.execute(
                            "select return_date from issue_book where ref_no =%s;", (self.Ref_no.get()))
                        result = cur.fetchall()

                        if len(result) != 0:
                            for row in result:
                                if row[0] is NULL:
                                    cur.execute(
                                        "UPDATE books_details SET rem_book = rem_book+1 WHERE book_name =(select book_name from issue_book where ref_no =%s);", (self.Ref_no.get()))

                        cur.execute(
                            "delete from issue_book where ref_no=%s", (self.Ref_no.get()))

                        sqlCon.commit()
                        self.Ref_no.set("")

                        sqlCon.close()
                        Display_Book()
                        Update(book_list)
                        Clear_Data()

                        messagebox.showinfo(
                            'Library Management System', 'Record Deleted Successfully')
                    else:
                        pass
                except:
                    messagebox.showerror(
                        'Library Management System', 'Data not Deleted..')
            else:
                messagebox.showerror(
                    'Library Management System', 'Please Select the Reference No From the Table.')

        #----- Function for Quit Window ----#

        def Qt_Win(event=""):
            qt = messagebox.askokcancel(
                'Library Management System', 'Are you sure you want to Quit?')
            if qt:
                self.root.destroy()
            else:
                pass

        #--- Pending Record Button Function ---#

        def Particular_User_Record_btn_f(event=""):
            Clear_Data()
            User_obj = Particular_User_Record_Class(username, dbpassword)

        #--- Pending Record Button Function ---#

        def Not_Returned_Book_btn_f(event=""):
            Clear_Data()
            Not_Returned_Book_obj = Not_Returned_Book_Class(
                username, dbpassword)

        #--- Member Record Button Function ---#

        def Data_Entry_btn_f(event=""):
            Clear_Data()
            Data_Entry_obj = Data_Entry_Class(username, dbpassword)

        #--- Member Record Button Function ---#

        def Member_Record_btn_f(event=""):
            Clear_Data()
            Member_Record_obj = Member_Record_Class(username, dbpassword)

        #--- Book Record Button Function ---#

        def Book_Record_btn_f(event=""):
            Clear_Data()
            Book_Record_obj = Book_Record_Class(username, dbpassword)

        def Lost_Book_Record_btn_f(event=""):
            Clear_Data()
            Lost_Book_Record_obj = Lost_Book_Class(username, dbpassword)


        def About_btn_f(event=""):
            Clear_Data()
            About_obj = About_Class()
        
        def Help_btn_f(event=""):
            Clear_Data()
            Help_obj = Help_Class()

        #--- Function for Importing Sql file ---#

        def Import_Sql_File():

            def parse_sql(sql_file_path):
                with open(sql_file_path, 'r', encoding='utf-8') as f:
                    data = f.read().splitlines()
                stmt = ''
                stmts = []
                for line in data:
                    if line:
                        if line.startswith('--'):
                            continue
                        stmt += line.strip() + ' '
                        if ';' in stmt:
                            stmts.append(stmt.strip())
                            stmt = ''
                return stmts

            yn = messagebox.askyesno(
                'Library Management System', 'The Current Database will be Deleted After The Import Process So Export your Current Database before Proceeding\n\nDo Not Use Application Before Completing The Importing Process.')
            if(not yn):
                return

            file_types = (('sql files', '*.sql'), ('All files', '*.*'))
            file_name = filedialog.askopenfilename(
                title='Open a SQL File', initialdir='/', filetypes=file_types)

            if file_name == "":
                return

            try:
                sqlCon = pymysql.connect(
                    host="localhost", user=username, password=dbpassword, database="lms")
                cur = sqlCon.cursor()
                cur.execute("DROP DATABASE IF EXISTS lms;")
                sqlCon = pymysql.connect(
                    host="localhost", user=username, password=dbpassword)
                cur = sqlCon.cursor()
                cur.execute("CREATE DATABASE lms")
                sqlCon.commit()
                sqlCon.close()
                conn = pymysql.connect(
                    host="localhost", user=username, password=dbpassword, database="lms")
                stmts = parse_sql(file_name)
                with conn.cursor() as cursor:
                    for stmt in stmts:
                        cursor.execute(stmt)
                    conn.commit()

                Clear_Data()
                Clear_Data()
                messagebox.showinfo('Library Management System',
                                    'Database imported Successfully.')

            except:
                messagebox.showerror(
                    'Library Management System', 'Wrong Database Imported.\nSo Reseting The Database...')
                Create_Database()
                Clear_Data()
                Clear_Data()
                messagebox.showinfo('Library Management System',
                                    'Reset Database Successfully.')

        #--- Function for Exporting Sql file ---#

        def export():
            try:
                file_types = (('sql files', '*.sql'), ('All files', '*.*'))
                dst = filedialog.asksaveasfilename(
                    title='Open a SQL File', initialdir='/', filetypes=file_types, defaultextension=".sql")

                if dst == "":
                    return

                if os.path.exists("C:/temp"):
                    shutil.rmtree("C:/temp")

                os.mkdir("C:/temp")
                os.system("mysqldump -u "+username+" lms > C:\\temp\\lms.sql")

                src = "C:/temp/lms.sql"

                shutil.copy2(src, dst)

                shutil.rmtree("C:/temp")

                messagebox.showinfo('Library Management System',
                                    'Export Database Successfully.')
            except:
                pass


        #--- Function for Lost Book ---#


        def Lost_Book_Btn(event=""):
    
            def SubmitBtn():
                if self.lost_bookname.get()=="" or self.lost_bookid.get()=="" or fineamount.get()=="":
                    messagebox.showerror('Library Management System', 'Please fill all the filds.', parent=top)
                    return
                elif int(fineamount.get())>=0 and int(fineamount.get())<=25000:
                    messagebox.showerror('Library Management System', '0 >= Fine Amount <= 25,000', parent=top)
                    return
                try:
                    sqlCon = pymysql.connect(host="localhost", user=username, password=dbpassword, database="lms")
                    cur = sqlCon.cursor()
                    cur.execute("INSERT INTO lost_book VALUES (%s,%s,%s);",(self.lost_bookid.get(),self.lost_bookname.get(),self.Lost_Date.get()))
                    sqlCon.commit()
                    sqlCon.close()
                    
                    messagebox.showinfo('Library Management System', 'Record Added Successfully.',parent=top)

                    try:
                        sqlCon = pymysql.connect(host="localhost", user=username, password=dbpassword, database="lms")
                        cur = sqlCon.cursor()

                        cur.execute("UPDATE issue_book SET return_date='0000-00-00' where book_id =%s and ref_no =(select ref_no from pending where book_id=%s);", (self.lost_bookid.get(),self.lost_bookid.get()))
                        cur.execute("UPDATE member_details SET amount= amount - %s where member_id = (select member_id from pending where book_id =%s);", (fineamount.get(),self.lost_bookid.get()))
                        cur.execute("DELETE FROM pending WHERE book_id = %s;", (self.lost_bookid.get()))

                        sqlCon.commit()
                        sqlCon.close()
                    except:
                        pass

                    
                except:
                    messagebox.showerror('Library Management System', 'Record Already Inserted Into Database.',parent=top)
                finally:
                    Clear_Data()
                    self.lost_bookname.set("")
                    self.lost_bookid.set("")
                    self.Lost_Date.set("")  
                    fineamount.set("")
                    Input_lost_book_id['value']=[]

            
            def Bookselect(event=""):
                try:
                    sqlCon = pymysql.connect(
                        host="localhost", user=username, password=dbpassword, database="lms")
                    cur = sqlCon.cursor()

                    cur.execute(
                        "select id_counter,no_book from books_details where book_name=%s;", (self.lost_bookname.get()))
                    result = cur.fetchall()

                    d1 = datetime.date.today()

                    bkid.clear()
                    self.lost_bookid.set("")

                    if len(result) != 0:
                        for row in result:
                            icount = int(row[0])
                            bcount = int(row[1])
                            self.Lost_Date.set(d1)

                        sqlCon.close()

                        for i in range(icount, icount+bcount):
                            bkid.append("%d" % i)

                        Input_lost_book_id['value'] = bkid
                except:
                    pass          

            
            top = Toplevel()
            top.grab_set()
            top.focus_force()

            fineamount=StringVar()
            
            Clear_Data()

            self.lost_bookname.set("")
            self.lost_bookid.set("")
            self.Lost_Date.set("")

            top.title("Library Management System | Lost Book")

            app_width = 550
            app_height = 300

            screen_width = top.winfo_screenwidth()
            screen_height = top.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-13)}')
            top.resizable(False, False)
            top.iconbitmap('icon.ico')

            frame = Frame(top)
            frame.place(relheight=1, relwidth=1)

            
            Lbl_Lost_Book_Name = Label(frame, text="Book Name:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=20).grid(row=0, column=0, sticky=W)

            cmbox=ttk.Combobox(frame, font=(
            "Comic Sans MS", 18, "bold",),textvariable=self.lost_bookname,state="readonly")
            cmbox.grid(row=0, column=1, sticky=W)
            cmbox['values'] = book_list
            cmbox.bind('<<ComboboxSelected>>', Bookselect)

            Lbl_Lost_Book_ID = Label(frame, text="Book Id:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=15).grid(row=1, column=0, sticky=W)
            Input_lost_book_id = ttk.Combobox(frame, font=(
            "Comic Sans MS", 18, "bold"), textvariable=self.lost_bookid, cursor="hand2", state="readonly")
            Input_lost_book_id.grid(row=1, column=1, sticky=W)
            Input_lost_book_id['values'] = []

            
            Lbl_Fine= Label(frame, text="Fine Amount:", font=(
            "Comic Sans MS",17, "bold"), padx=20, pady=15).grid(row=2, column=0, sticky=W)
            Input_Fine = ttk.Entry(frame, font=(
            "Comic Sans MS", 18, "bold"), width=21,textvariable=fineamount).grid(row=2, column=1, sticky=W)


            Btn_Return_Book = Button(frame, text="Submit", width=15, bg="#000716", cursor="hand2", fg="white", font=(
                "Comic Sans MS", 15, "bold"), command=SubmitBtn).place(x=180, y=220)


        #--- Function for Lost Book ---#


        def Modify_Book_Btn(event=""):
    
            def SubmitBtn():
                if self.Add_Book_Name.get() == "" or  self.Add_Book_Count.get()=="":
                    messagebox.showerror('Library Management System', 'Please fill all the filds.', parent=top)
                    return
                try:
                    sqlCon = pymysql.connect(host="localhost", user=username, password=dbpassword, database="lms")
                    cur = sqlCon.cursor()

                    cur.execute("select no_book from books_details where book_name= %s;",(self.Add_Book_Name.get()))
                    result = cur.fetchall()

                    no=0
                    if len(result) != 0:
                        for row in result:
                            no=row[0]
                    
                    no=int(no)+int(self.Add_Book_Count.get())

                    if no >=100:
                        messagebox.showerror('Library Management System', 'Total Number Of Book Should be Less Than 100.',parent=top)
                        Clear_Data()
                        return

                    cur.execute("UPDATE books_details SET no_book=no_book + %s , rem_book=rem_book + %s WHERE book_name=%s and no_book + %s < 100;",(self.Add_Book_Count.get(),self.Add_Book_Count.get(),self.Add_Book_Name.get(),self.Add_Book_Count.get()))
                    sqlCon.commit()
                    sqlCon.close()
                    messagebox.showinfo('Library Management System', 'Book Update Successfully.',parent=top)
                    Clear_Data()
                except:
                    pass

            
            top = Toplevel()
            top.grab_set()
            top.focus_force()
            
            Clear_Data()

            

            top.title("Library Management System | Modify Book")

            app_width = 600
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

            
            Lbl_Modify_Book_Name = Label(frame, text="Book Name:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=20).grid(row=0, column=0, sticky=W)

            cmbox=ttk.Combobox(frame, font=(
            "Comic Sans MS", 18, "bold",),textvariable=self.Add_Book_Name,state="readonly")
            cmbox.grid(row=0, column=1, sticky=W)
            cmbox['values'] = book_list


            Lbl_Book_Count = Label(frame, text="Number Of Books:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=15).grid(row=1, column=0, sticky=W)
            
            Input_Book_Count = ttk.Spinbox(frame,state="readonly",textvariable=self.Add_Book_Count, font=("Comic Sans MS", 18, "bold"), from_=1, to=20, wrap=True)
            Input_Book_Count.grid(row=1, column=1, sticky=W)

            Btn_Return_Book = Button(frame, text="Submit", width=15, bg="#000716", cursor="hand2", fg="white", font=(
                "Comic Sans MS", 15, "bold"), command=SubmitBtn).place(x=200, y=175)



        def Send_Reminder_Mail():

            def send_mail(mail):
                try:
                    port = 587  # For SSL
                    host = "smtp-mail.outlook.com"
                    sender_email = "librarymanagementsystemproject@outlook.com"  # Enter your address
                    receiver_email = self.Ml.get() # Enter receiver address
                    password = "lms@1234"
                    receiver_email = mail # Enter receiver address
                    
                    xyz=dt.get()
                    xyz=xyz[8:10]+xyz[4]+xyz[5:7]+xyz[4]+xyz[0:4]

                    subject="Reminder For Return Book"
                    body="Kindly return the book which you have taken from our library.\nThe due date is : "+xyz
                    

                    message = f'Subject: {subject}\n\n{body}'

                    server = smtplib.SMTP(host, port)
                    server.starttls()
                    server.login(sender_email, password)
                    output = server.sendmail(sender_email, receiver_email, message)

                except:
                    pass
            
            d1 = datetime.date.today()
            d2 = datetime.timedelta(days=2)
            dt = StringVar()
            dt.set(d1+d2)
            
            lst=[]

            sqlCon = pymysql.connect(host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            cur.execute("select mail from member_details where member_id in (SELECT `member_id` FROM `issue_book` WHERE `return_date` is NULL and due_date=%s);",(dt.get()))
            result = cur.fetchall()
            
            if len(result) != 0:
                for row in result:
                    lst.append(row[0])
            sqlCon.close()

            if len(lst)==0:
                return

            messagebox.showinfo('Library Management System', 'Sending Mail Please Wait....\n\nDO NOT Press Any Key Before The Next Popup Message Will Come.')
            for i in range(len(lst)):
                send_mail(lst[i])
            
            messagebox.showinfo('Library Management System', 'Send Reminder Successfully.')
            

## --------------------- Function For Title Bar ----------------------- ##

        #---- Function For Changing Time ----#

        def tick():
            global time1
            time2 = time.strftime('%I:%M:%S %p')
            clock.config(text=time2)
            clock.after(200, tick)


## --------------------- Function For Info Frame Left ----------------------- ##

        #------ Autofill member details for dashboard -----#


        def Autofill(event=""):
            try:
                if(len(event.widget.get())) >= 4:
                    try:
                        sqlCon = pymysql.connect(
                            host="localhost", user=username, password=dbpassword, database="lms")
                        cur = sqlCon.cursor()

                        cur.execute(
                            "select member_type,member_id,first_name,last_name,address,dept,mail,mobile,amount from member_details where member_id=%s;", (event.widget.get()))
                        result = cur.fetchall()

                        if len(result) != 0:
                            for row in result:
                                self.Member_Type.set(row[0])
                                self.Member_ID.set(row[1])
                                self.First_Name.set(row[2])
                                self.Last_Name.set(row[3])
                                self.Address.set(row[4])
                                self.Dept.set(row[5])
                                self.Mail.set(row[6])
                                self.Ph.set(row[7])
                                self.Cur_Amount.set(row[8])
                        else:
                            self.Member_Type.set("")
                            self.First_Name.set("")
                            self.Last_Name.set("")
                            self.Address.set("")
                            self.Dept.set("")
                            self.Mail.set("")
                            self.Ph.set("")
                            self.Cur_Amount.set("")

                        sqlCon.close()

                    except:
                        pass
                else:
                    self.Member_Type.set("")
                    self.First_Name.set("")
                    self.Last_Name.set("")
                    self.Address.set("")
                    self.Dept.set("")
                    self.Mail.set("")
                    self.Ph.set("")
                    self.Cur_Amount.set("")
            except:
                pass


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

        #---- Select Book Function -----#

        def Select_Book(event=""):
            try:
                value = str(book_ListBox.get((book_ListBox.curselection())))
                sqlCon = pymysql.connect(
                    host="localhost", user=username, password=dbpassword, database="lms")
                cur = sqlCon.cursor()

                cur.execute(
                    "select book_name,book_sub,author,shelf_no,id_counter,no_book from books_details where book_name=%s;", value)
                result = cur.fetchall()

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)

                bkid.clear()
                Input_Book_ID.set("")

                if len(result) != 0:
                    for row in result:
                        self.Book_Name.set(row[0])
                        self.Book_Subject.set(row[1])
                        self.Author_Name.set(row[2])
                        self.shelf_no.set(row[3])
                        icount = int(row[4])
                        bcount = int(row[5])
                        self.Issue_Date.set(d1)
                        self.Due_Date.set(d1+d2)

                    sqlCon.commit()
                    sqlCon.close()

                    for i in range(icount, icount+bcount):
                        bkid.append("%d" % i)

                    Input_Book_ID['value'] = bkid
            except:
                pass

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
            Input_Book_ID['value'] = []


## --------------------- Function Of Button Frame ----------------------- ##

        #--- Add Data Button Function ---#


        def Add_Data(event=""):
            if self.Member_ID.get() == "" or self.Book_ID.get() == "" or self.Book_ED.get() == "" or self.Issue_Date.get() == "" or self.Due_Date.get() == "":
                messagebox.showerror(
                    'Library Management System', 'Please Fill All The Required Input Details.')
                return
            else:
                try:
                    
                    datetime_str1 = datetime.datetime.strptime(self.Issue_Date.get(),'%Y-%m-%d')
                    try:
                        datetime_str2 = datetime.datetime.strptime(self.Due_Date.get(),'%Y-%m-%d')
                    except:
                        messagebox.showerror('Library Management System', 'Invalid Due-Date Format.')
                        return


                    vl=datetime_str2-datetime_str1
                    
                    if(str(vl)[0]=="-"):
                        messagebox.showerror('Library Management System', 'Due-Date Should Not Be Less Than Issue-Date.')
                        return
                    
                    
                    sqlCon = pymysql.connect(
                        host="localhost", user=username, password=dbpassword, database="lms")
                    cur = sqlCon.cursor()

                    if int(self.Cur_Amount.get()) <= 0:
                        messagebox.showerror('Library Management System', 'The Current Amount of This Member Id :' +
                                             self.Member_ID.get()+' Is too Low.\n\nThe Current Amount is : '+self.Cur_Amount.get())
                        return

                    cur.execute(
                        "select * from pending where book_id= %s;", (self.Book_ID.get()))
                    result = cur.fetchall()

                    if len(result) != 0:
                        messagebox.showerror(
                            'Library Management System', 'This Book Is Not Available')
                        return
                    
                    cur.execute(
                        "select * from lost_book where book_id= %s;", (self.Book_ID.get()))
                    result = cur.fetchall()

                    if len(result) != 0:
                        messagebox.showerror(
                            'Library Management System', 'This Book Is Not Available')
                        return

                    try:
                        cur.execute("insert into pending values (%s,%s,%s);", (self.Member_ID.get(
                        ), self.Member_ID.get()+self.Issue_Date.get().replace("-", ""), self.Book_ID.get()))
                    except:
                        messagebox.showerror('Library Management System', 'Member id :' +
                                             self.Member_ID.get()+' not returned the previous book.')
                        return

                    try:
                        cur.execute("insert into issue_book (ref_no,member_id,book_id,book_name,book_ed,issue_date,due_date) values (%s,%s,%s,%s,%s,%s,%s);", (self.Member_ID.get(
                        )+self.Issue_Date.get().replace("-", ""), self.Member_ID.get(), self.Book_ID.get().upper(), self.Book_Name.get(), self.Book_ED.get(), self.Issue_Date.get(), self.Due_Date.get()))
                    except:
                        messagebox.showerror(
                            'Library Management System', 'Member id :'+self.Member_ID.get()+' already assigned a book today.')
                        return

                    cur.execute("insert into serial (ref_no) values (%s);", (self.Member_ID.get(
                    )+self.Issue_Date.get().replace("-", "")))
                    sqlCon.commit()

                    cur.execute(
                        "update books_details set rem_book = rem_book - 1 where book_name=%s;", (self.Book_Name.get()))  # add
                    sqlCon.commit()

                    rno = self.Member_ID.get()+self.Issue_Date.get().replace("-", "")

                    try:
                        port = 587  # For SSL
                        host = "smtp-mail.outlook.com"
                        sender_email = "librarymanagementsystemproject@outlook.com"  # Enter your address
                        receiver_email = self.Mail.get() # Enter receiver address
                        password = "lms@1234"

                        subject="Issued Book Confirmation"
                        body="Thanks For Issued Book From Our Library Management System.\n\nMembership Information:\n\nMember ID: "+self.Member_ID.get()+"\nMember Type : "+self.Member_Type.get()+" \nFirst Name : "+self.First_Name.get()+" \nLast Name : "+self.Last_Name.get()+"\nMail ID : "+self.Mail.get()+" \nCurrent Amount : "+self.Cur_Amount.get()+" \n\nBook Information:\n\nReferance No: "+rno+"\nBook ID: "+self.Book_ID.get()+"\nBook Name: "+self.Book_Name.get()+"\nBook Ed: "+self.Book_ED.get()+"\nAuthor: "+self.Author_Name.get()+"\nIssue Date: "+self.Issue_Date.get()+"\nDue Date: "+self.Due_Date.get()+"\n\n\nPlease Return This Book Within The Due Date"

                        

                        message = f'Subject: {subject}\n\n{body}'

                        server = smtplib.SMTP(host, port)
                        server.starttls()
                        server.login(sender_email, password)
                        output = server.sendmail(sender_email, receiver_email, message)

                    except:
                        pass

                    sqlCon.close()
                    Clear_Data()
                    Update(book_list)
                    messagebox.showinfo(
                        'Library Management System', 'Record Entered Successfully.\nThe Reference No Is : '+rno)
                    rno = ""

                except:
                    pass

        #---- Clear Data Button Function For Dashboard ----#

        def Clear_Data(event=""):
            self.Member_Type.set("")
            self.Member_ID.set("")
            self.First_Name.set("")
            self.Last_Name.set("")
            self.Address.set("")
            self.Dept.set("")
            self.Mail.set("")
            self.Ph.set("")

            bkid.clear()
            Input_Book_ID['value'] = bkid

            self.Book_ID.set("")
            self.Book_Name.set("")
            self.Book_ED.set("")
            self.Book_Subject.set("")
            self.Author_Name.set("")
            self.shelf_no.set("")
            self.Issue_Date.set("")
            self.Due_Date.set("")
            self.Cur_Amount.set("")

            self.entry.set("")

            self.Add_Book_Name.set("")
            self.Add_Book_Count.set("")
            self.Add_Book_Subject.set("")
            self.Add_Author_Name.set("")

            self.Ref_no.set("")
            self.Book_ret.set("")
            self.Ret_B_Id.set("")
            self.D_Date.set("")

            self.M_Type.set("")
            self.F_Name.set("")
            self.L_Name.set("")
            self.Add.set("")
            self.Dt.set("")
            self.Phone.set("")
            self.C_Amount.set("")
            self.St.set("")
            self.lost_bookname.set("")
            self.lost_bookid.set("")
            self.Lost_Date.set("")

            Update(book_list)
            Display_Data()
            Display_Book()
            Input_Member_ID.focus()

        #--- Add Member Button Function ---#

        def Add_Member_btn_f(event=""):
            Clear_Data()
            new_obj = Add_Member_Class(username, dbpassword)

        #---- Function for Add Book Button -----#

        def Add_Book_btn_f(event=""):

            #---- Function for Book subject CMB Search -----#
            def check_input(event):
                value = event.widget.get()

                if value == '':
                    Input_Add_Book_Subject['values'] = bsub
                else:
                    data = []
                    for item in bsub:
                        if value.lower() in item.lower():
                            data.append(item)

                    Input_Add_Book_Subject['values'] = data

            #---- Function for Add Book Submit Button -----#

            def Add_Book(event=""):
                if self.Add_Book_Name.get() == "" or self.Add_Book_Subject.get() == "" or self.Add_Author_Name.get() == "" or self.Add_Book_Count.get() == "" or self.shelf_no.get() == "" :
                    messagebox.showerror(
                        'Library Management System', 'Please Enter All Details', parent=top)
                elif not self.Add_Author_Name.get().replace(' ','').isalpha():
                    messagebox.showerror('Library Management System', 'Author Name should not contain any special characters or number.', parent=top)
                    return
                else:
                    try:
                        sqlCon = pymysql.connect(
                            host="localhost", user=username, password=dbpassword, database="lms")
                        cur = sqlCon.cursor()

                        cur.execute(
                            "select max(id_counter) from books_details")
                        result = cur.fetchall()

                        if len(result) != 0:
                            for row in result:
                                id_counter = (row[0])

                        if id_counter is None:
                            id_counter = 1

                        cur.execute("insert into books_details (book_name,book_sub,author,shelf_no,no_book,rem_book,id_counter) values (%s,%s,%s,%s,%s,%s,%s);", (self.Add_Book_Name.get().title(
                        ).strip()+' By '+self.Add_Author_Name.get().title().strip(), self.Add_Book_Subject.get().title().strip(), self.Add_Author_Name.get().title().strip(), self.shelf_no.get().upper().strip(), self.Add_Book_Count.get(), self.Add_Book_Count.get(), str(int(id_counter)+100)))

                        xy=int(id_counter)+100
                        z=self.Add_Book_Count.get()

                        sqlCon.commit()
                        sqlCon.close()

                        Display_Book()
                        Update(book_list)

                        
                        
                        st=""

                        for i in range(int(z)-1):
                            st=st+str(xy)+", "
                            xy+=1
                        st=st+str(xy)+" "
                        
                        messagebox.showinfo(
                            'Library Management System', "Book Added Successfully.\n\nThe Book Id's are:\n\n"+st, parent=top)
                        Clear_Data()
                    

                    except:
                        messagebox.showerror('Library Management System', 'The book : ' +
                                             self.Add_Book_Name.get().title()+' Already Exists.', parent=top)
                        Clear_Data()

            #---------- CODE FOR ADD BOOK WINDOW -------------#

            top = Toplevel()
            top.grab_set()

            top.title("Library Management System | Add Book")
            Clear_Data()
            app_width = 550
            app_height = 400
            screen_width = top.winfo_screenwidth()
            screen_height = top.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-50)}')
            top.resizable(False, False)
            top.iconbitmap('icon.ico')
            frame = Frame(top)
            frame.place(relheight=1, relwidth=1)

            Lbl_Add_Book_Name = Label(frame, text="Book Name:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=10).grid(row=0, column=0, sticky=W)
            Input_Add_Book_Name = ttk.Entry(frame, font=(
                "Comic Sans MS", 17, "bold"), textvariable=self.Add_Book_Name)
            Input_Add_Book_Name.grid(row=0, column=1, sticky=W)
            Input_Add_Book_Name.bind(
                "<Return>", lambda funct1: Input_Add_Book_Subject.focus())
            Input_Add_Book_Name.focus()

            Lbl_Add_Book_Subject = Label(frame, text="Book Subject:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=10).grid(row=1, column=0, sticky=W)
            Input_Add_Book_Subject = ttk.Combobox(frame, font=(
                "Comic Sans MS", 16, "bold"), textvariable=self.Add_Book_Subject, width=20)
            Input_Add_Book_Subject.grid(row=1, column=1, sticky=W)
            Input_Add_Book_Subject.bind(
                "<Return>", lambda funct1: Input_Add_Author_Name.focus())
            Input_Add_Book_Subject['values'] = bsub
            Input_Add_Book_Subject.bind('<KeyRelease>', check_input)

            Lbl_Add_Author_Name = Label(frame, text="Author Name:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=10).grid(row=2, column=0, sticky=W)
            Input_Add_Author_Name = ttk.Entry(frame, font=(
                "Comic Sans MS", 17, "bold"), textvariable=self.Add_Author_Name)
            Input_Add_Author_Name.grid(row=2, column=1, sticky=W)
            Input_Add_Author_Name.bind(
                "<Return>", lambda funct1: Input_Add_Shelf_no.focus())

            Lbl_Add_Shelf_no = Label(frame, text="Bookshelf No:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=10).grid(row=3, column=0, sticky=W)
            Input_Add_Shelf_no = ttk.Entry(frame, font=(
                "Comic Sans MS", 17, "bold"), textvariable=self.shelf_no)
            Input_Add_Shelf_no.grid(row=3, column=1, sticky=W)
            Input_Add_Shelf_no.bind(
                "<Return>", lambda funct1: Input_Add_Book_Count.focus())

            Lbl_Add_Book_Count = Label(frame, text="Number Of Book", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=10).grid(row=4, column=0, sticky=W)

            Input_Add_Book_Count = ttk.Spinbox(frame,state="readonly", font=(
                "Comic Sans MS", 17, "bold"), textvariable=self.Add_Book_Count, from_=1, to=20, wrap=True, width=19)
            Input_Add_Book_Count.grid(row=4, column=1, sticky=W)

            Btn_Add_Book = Button(frame, text="Submit", width=15, bg="#000716", cursor="hand2", fg="white", font=(
                "Comic Sans MS", 15, "bold"), command=Add_Book).place(x=175, y=300)

        #---- Function for Return Book Button -----#

        def Return_Book_btn_f(event=""):

            #---- Function for Return Book Autofill -----#

            def R_Book_Autofill(event=""):
                try:
                    if(len(event.widget.get())) >= 13:
                        try:
                            sqlCon = pymysql.connect(
                                host="localhost", user=username, password=dbpassword, database="lms")
                            cur = sqlCon.cursor()

                            cur.execute(
                                "select  ref_no, book_id, due_date from issue_book where ref_no=%s;", (event.widget.get()))
                            result = cur.fetchall()

                            if len(result) != 0:
                                for row in result:
                                    self.Ref_no.set(row[0]),
                                    self.Ret_B_Id.set(row[1]),
                                    self.D_Date.set(row[2]),
                                    self.Book_ret.set(datetime.date.today()),
                                sqlCon.close()
                            else:
                                self.Ret_B_Id.set(""),
                                self.D_Date.set(""),
                                self.Book_ret.set(""),
                                sqlCon.close()
                        except:
                            pass
                    else:
                        self.Ret_B_Id.set(""),
                        self.D_Date.set(""),
                        self.Book_ret.set("")
                except:
                    pass

            #---- Function for Return Book Submit Button -----#

            def Btn_Ret_B():
                if self.Ref_no.get() == "" or self.Ret_B_Id.get() == "":
                    messagebox.showerror(
                        'Library Management System', 'Please Fill All The Fields.', parent=top)
                else:
                    try:
                        sqlCon = pymysql.connect(
                            host="localhost", user=username, password=dbpassword, database="lms")
                        cur = sqlCon.cursor()

                        cur.execute(
                            "select return_date from issue_book where ref_no =%s;", (self.Ref_no.get()))
                        result = cur.fetchall()

                        if len(result) != 0:
                            for row in result:
                                if row[0] is None:
                                    cur.execute(
                                        "UPDATE issue_book SET return_date=%s where ref_no =%s;", (self.Book_ret.get(), self.Ref_no.get()))
                                    cur.execute(
                                        "DELETE FROM pending WHERE ref_no =%s;", (self.Ref_no.get()))

                                    date_format = "%Y-%m-%d"
                                    a = datetime.datetime.strptime(
                                        self.D_Date.get(), date_format)
                                    b = datetime.datetime.strptime(
                                        self.Book_ret.get(), date_format)
                                    c = (a-b).days
                                    if(c < 0):
                                        cur.execute(
                                            "UPDATE member_details SET amount= amount + %s where member_id = (select member_id from issue_book where ref_no =%s);", (c, self.Ref_no.get()))

                                    cur.execute(
                                        "UPDATE books_details SET rem_book = rem_book + 1 WHERE book_name =(select book_name from issue_book where ref_no =%s);", (self.Ref_no.get()))

                                    sqlCon.commit()
                                    sqlCon.close()

                                    messagebox.showinfo(
                                        'Library Management System', 'Book Submitted Successfully.', parent=top)
                                    Display_Book()
                                    Update(book_list)
                                    Clear_Data()
                                else:
                                    sqlCon.close()
                                    messagebox.showerror(
                                        'Library Management System', 'Book Already Submitted.', parent=top)
                                    Clear_Data()

                    except:
                        sqlCon.close()

            #---------- CODE FOR RETURN BOOK WINDOW -------------#

            top = Toplevel()
            top.grab_set()

            top.title("Library Management System | Return Book")
            Clear_Data()
            app_width = 500
            app_height = 400
            screen_width = top.winfo_screenwidth()
            screen_height = top.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-50)}')
            top.resizable(False, False)
            top.iconbitmap('icon.ico')
            frame = Frame(top)
            frame.place(relheight=1, relwidth=1)

            self.Ref_no.set("")
            Lbl_Ref_No = Label(frame, text="Reference No:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=20).grid(row=0, column=0, sticky=W)

            Input_Ref_No = ttk.Entry(frame, font=(
                "Comic Sans MS", 16, "bold"), textvariable=self.Ref_no)
            Input_Ref_No.grid(row=0, column=1, sticky=W)
            Input_Ref_No.bind(
                "<Return>", lambda funct1: Input_Ret_Date.focus())
            Input_Ref_No.focus()
            Input_Ref_No.bind('<KeyRelease>', R_Book_Autofill)

            Lbl_B_Id = Label(frame, text="Book Id:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=15).grid(row=1, column=0, sticky=W)

            Input_B_Id = ttk.Entry(frame, font=(
                "Comic Sans MS", 16, "bold"), textvariable=self.Ret_B_Id, state='disabled').grid(row=1, column=1, sticky=W)

            Lbl_D_Date = Label(frame, text="Due Date:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=15).grid(row=2, column=0, sticky=W)

            Input_D_Date = ttk.Entry(frame, font=(
                "Comic Sans MS", 16, "bold"), textvariable=self.D_Date, state='disabled').grid(row=2, column=1, sticky=W)

            Lbl_Ret_Date = Label(frame, text="Return Date:", font=(
                "Comic Sans MS", 17, "bold"), padx=20, pady=15).grid(row=3, column=0, sticky=W)

            Input_Ret_Date = ttk.Entry(frame, font=(
                "Comic Sans MS", 16, "bold"), textvariable=self.Book_ret)
            Input_Ret_Date.grid(row=3, column=1, sticky=W)
            Input_Ret_Date.bind("<Return>", lambda funct1: Btn_Ret_B())

            Btn_Return_Book = Button(frame, text="Submit", width=15, bg="#000716", cursor="hand2", fg="white", font=(
                "Comic Sans MS", 15, "bold"), command=Btn_Ret_B).place(x=150, y=300)


## --------------------- Function For Data Frame ----------------------- ##

        #---- Display Data Function to Display All record on the dashboard in form of Table ----#


        def Display_Data(event=""):
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()

            cur.execute("select s.sr_no,i.ref_no,m.member_type,m.member_id,m.first_name,m.last_name,m.address,m.mail,m.mobile,i.book_id,i.book_name,i.book_ed,b.book_sub,b.author,b.shelf_no,i.issue_date,i.due_date,i.return_date,m.amount from issue_book as i,books_details as b,member_details as m,serial as s where i.member_id=m.member_id and i.book_name=b.book_name and s.ref_no=i.ref_no order by s.sr_no desc;")
            result = cur.fetchall()

            if len(result) != 0:
                self.library_table.delete(*self.library_table.get_children())

                for row in result:
                    self.library_table.insert('', END, values=row)

                sqlCon.commit()
                sqlCon.close()
            else:
                sqlCon.close()
                self.library_table.delete(*self.library_table.get_children())

        #---- Get cursor function for selecting record in table ----#

        def Get_Cursor(event=""):
            try:
                cursor_row = self.library_table.focus()
                content = self.library_table.item(cursor_row)
                r = content['values']
                self.Ref_no.set(r[1])
                self.Member_Type.set(r[2])
                self.Member_ID.set(r[3])
                self.First_Name.set(r[4])
                self.Last_Name.set(r[5])
                self.Address.set(r[6])
                self.Mail.set(r[7])
                self.Ph.set(r[8])
                self.Book_ID.set(r[9])
                self.Book_Name.set(r[10])
                self.Book_ED.set(r[11])
                self.Book_Subject.set(r[12])
                self.Author_Name.set(r[13])
                self.shelf_no.set(r[14])
                self.Issue_Date.set(r[15])
                self.Due_Date.set(r[16])
                self.Cur_Amount.set(r[18])
            except:
                pass


## --------------------- Extra Function For Sideloaded ----------------------- ##

        # ---- Create Database Function ---- #


        def Create_Database():
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword)
            cur = sqlCon.cursor()
            cur.execute("DROP DATABASE IF EXISTS lms;")
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword)
            cur = sqlCon.cursor()
            cur.execute("CREATE DATABASE lms")
            sqlCon.commit()
            sqlCon.close()
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()
            cur.execute("CREATE TABLE books_details ( book_name varchar(100) NOT NULL, book_sub varchar(20) NOT NULL, author varchar(20) NOT NULL, shelf_no varchar(5) NOT NULL, no_book int NOT NULL, rem_book int NOT NULL, id_counter int NOT NULL);")
            sqlCon.commit()
            cur.execute("CREATE TABLE issue_book ( ref_no varchar(30) NOT NULL, member_id int NOT NULL, book_id varchar(10) NOT NULL, book_name varchar(100) NOT NULL, book_ed varchar(10) NOT NULL, issue_date date NOT NULL, due_date date NOT NULL,return_date date DEFAULT NULL);")
            sqlCon.commit()
            cur.execute("CREATE TABLE member_details ( member_type varchar(10) NOT NULL,  member_id int NOT NULL,  first_name varchar(20) NOT NULL,  last_name varchar(20) NOT NULL,  address varchar(50) NOT NULL,  dept varchar(30) NOT NULL,  mail varchar(50) NOT NULL,  mobile varchar(20) NOT NULL,  amount int NOT NULL DEFAULT 0, password varchar(50) NOT NULL);")
            sqlCon.commit()
            cur.execute(
                "CREATE TABLE pending (member_id int NOT NULL,  ref_no varchar(30) NOT NULL,  book_id varchar(10) NOT NULL);")
            sqlCon.commit()
            cur.execute(
                "CREATE TABLE serial (ref_no varchar(30) NOT NULL, sr_no int NOT NULL);")
            sqlCon.commit()
            cur.execute(
                "CREATE TABLE lost_book (book_id varchar(10) NOT NULL, book_name varchar(100) NOT NULL, lost_date date DEFAULT NULL);")
            sqlCon.commit()
            cur.execute(
                "ALTER TABLE books_details ADD PRIMARY KEY (book_name);")
            sqlCon.commit()
            cur.execute(
                "ALTER TABLE lost_book ADD PRIMARY KEY (book_id);")
            sqlCon.commit()
            cur.execute(
                "ALTER TABLE issue_book ADD PRIMARY KEY (ref_no,book_name), ADD UNIQUE KEY ref_no (ref_no);")
            sqlCon.commit()
            cur.execute(
                "ALTER TABLE member_details ADD PRIMARY KEY (member_id), ADD UNIQUE KEY mail (mail), ADD UNIQUE KEY mobile (mobile);")
            sqlCon.commit()
            cur.execute("ALTER TABLE pending ADD PRIMARY KEY (member_id);")
            sqlCon.commit()
            cur.execute("ALTER TABLE serial ADD PRIMARY KEY (sr_no);")
            sqlCon.commit()
            cur.execute(
                "ALTER TABLE member_details MODIFY member_id int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10001;")
            sqlCon.commit()
            cur.execute(
                "ALTER TABLE serial MODIFY sr_no int NOT NULL AUTO_INCREMENT;")
            sqlCon.commit()
            cur.execute(
                "ALTER TABLE issue_book ADD FOREIGN KEY (member_id) REFERENCES member_details (member_id);")
            sqlCon.commit()
            cur.execute(
                "ALTER TABLE lost_book ADD FOREIGN KEY (book_name) REFERENCES books_details (book_name);")
            sqlCon.commit()
            cur.execute(
                "ALTER TABLE pending ADD FOREIGN KEY (member_id) REFERENCES member_details (member_id);")
            sqlCon.commit()
            cur.execute(
                "ALTER TABLE serial ADD FOREIGN KEY (ref_no) REFERENCES issue_book (ref_no);")
            sqlCon.commit()
            sqlCon.close()

            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database="lms")
            cur = sqlCon.cursor()
            cur.execute(
                "CREATE USER IF NOT EXISTS 'user'@'localhost' IDENTIFIED BY '1234';")
            sqlCon.commit()
            cur.execute("GRANT ALL ON *.* TO 'user'@'localhost';")
            sqlCon.commit()
            cur.execute("FLUSH PRIVILEGES;")
            sqlCon.commit()
            sqlCon.close()


## --------------------------- Instance Valiable For The Class Admin Panel ------------------- ##

        self.root = root

        self.Member_Type = StringVar()
        self.Member_ID = StringVar()
        self.First_Name = StringVar()
        self.Last_Name = StringVar()
        self.Address = StringVar()
        self.Cur_Amount = StringVar()
        self.Dept = StringVar()
        self.Mail = StringVar()
        self.Ph = StringVar()

        self.Book_ID = StringVar()
        bkid = []
        self.Book_Name = StringVar()
        self.Book_ED = StringVar()
        self.Book_Subject = StringVar()
        bsub = []
        self.Author_Name = StringVar()
        self.shelf_no = StringVar()
        self.Issue_Date = StringVar()
        self.Due_Date = StringVar()

        self.Add_Book_Name = StringVar()
        self.Add_Book_Count = StringVar()
        self.Add_Book_Subject = StringVar()
        self.Add_Author_Name = StringVar()

        self.entry = StringVar()
        book_list = []

        self.Ref_no = StringVar()

        self.Book_ret = StringVar()
        self.Ret_B_Id = StringVar()
        self.D_Date = StringVar()

        self.M_Type = StringVar()
        self.M_Id = StringVar()
        self.F_Name = StringVar()
        self.L_Name = StringVar()
        self.Add = StringVar()
        self.Dt = StringVar()
        self.Phone = StringVar()
        self.C_Amount = StringVar()
        self.Ml = StringVar()
        self.St = StringVar()
        
        self.lost_bookname=StringVar()
        self.lost_bookid=StringVar()
        self.Lost_Date=StringVar()

        self.val=0

## -------------------- Dash Board Window Size --------------------- ##

        self.root.title("Library Management System")  # Title of the app
        self.root.attributes('-fullscreen', True)
        self.root.after(1, lambda: Input_Member_ID.focus_force())
        ht = self.root.winfo_screenheight()  # Height of the Window
        wt = self.root.winfo_screenwidth()  # Width of the Window
        # Setting geometry of main screen
        self.root.geometry("%dx%d+%d+%d" % (wt, ht, 0, 0))

        #--------------------------Database Check ------------------------#

        try:
            sqlCon = pymysql.connect(
                host="localhost", user=username, password=dbpassword, database='lms')
        except:
            Create_Database()

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
            label="Refresh", accelerator="Esc", command=Clear_Data)
        self.root.bind("<Escape>", Clear_Data)
        edit_menu.add_separator()
        edit_menu.add_command(label="Add Member",
                              accelerator="Ctrl+M", command=Add_Member_btn_f)
        self.root.bind("<Control_L><m>", Add_Member_btn_f)
        edit_menu.add_command(label="Modify Member", command=Mod_Member_btn_f)

        edit_menu.add_separator()

        sub_menu = Menu(edit_menu, tearoff=0)
        sub_menu.add_command(label='Lost Book',command=Lost_Book_Btn)
        sub_menu.add_command(label='Update Book Details',command=Modify_Book_Btn)

        edit_menu.add_cascade(label="Modify Books",menu=sub_menu)

        edit_menu.add_separator()
        edit_menu.add_command(label="Delete Record",
                              accelerator="Ctrl+D", command=delete_data)
        self.root.bind("<Control_L><d>", delete_data)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        show_menu = Menu(menubar, tearoff=0)
        show_menu.add_command(label="Perticular Day Record", command=Data_Entry_btn_f)
        show_menu.add_separator()
        show_menu.add_command(label="Particular Members's Record",
                              command=Particular_User_Record_btn_f)
        show_menu.add_command(label="Not Returned Book",
                              command=Not_Returned_Book_btn_f)
        show_menu.add_separator()
        show_menu.add_command(label="Show Lost Books",
                              command=Lost_Book_Record_btn_f)
        show_menu.add_separator()                    
        show_menu.add_command(label="All Members Record",
                              command=Member_Record_btn_f)
        show_menu.add_command(label="All Books Record",
                              command=Book_Record_btn_f)
                              
        menubar.add_cascade(label="Show", menu=show_menu)

        send_menu = Menu(menubar, tearoff=0)
        send_menu.add_command(label="Send Reminder",
                                command=Send_Reminder_Mail)
        menubar.add_cascade(label="Reminder", menu=send_menu)
        

        import_menu = Menu(menubar, tearoff=0)
        import_menu.add_command(label="Import SQL File",
                                command=Import_Sql_File)
        menubar.add_cascade(label="Import", menu=import_menu)

        export_menu = Menu(menubar, tearoff=0)
        export_menu.add_command(label="Export As SQL", command=export)
        menubar.add_cascade(label="Export", menu=export_menu)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Help", accelerator="F1",command=Help_btn_f)
        self.root.bind("<F1>", Help_btn_f)
        help_menu.add_command(
            label="About", command=About_btn_f)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)


## --------------------- Title Bar ------------------ ##

        Title = Label(self.root, text="Library Management System", fg="#000716", bd=15, relief=RIDGE,
                      font=("Comic Sans MS", 35, "bold"), padx=2, pady=6)
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
            frame.place(x=0, y=105, width=wt, height=400)
        else:
            frame.place(x=0, y=105, width=wt, height=345)


# ------------------------------ Info_Frame_Left --------------------------#

        Info_Frame_Left = LabelFrame(frame, text="Library Membership Information", fg="#000716", bd=10, relief=RIDGE,
                                     font=("Comic Sans MS", 14, "bold"))
        # Screen Size Adjustment
        if wt > 1400:
            Info_Frame_Left.place(x=0, y=5, width=wt *
                                  (2 / 3) - 120, height=360)
            fsize = 14
            ewidthleft = 21
            ewidthright = 20
            py = 4
            xy=3
            yx=2

        else:
            Info_Frame_Left.place(x=0, y=5, width=wt *
                                  (2 / 3) - 120, height=305)
            fsize = 12
            ewidthleft = 21
            ewidthright = 21
            py = 3
            xy=2
            yx=0

        # ------- Label and Input Field for Left side of the Info_Frame_Left ------- #

        Lbl_Member_Type = Label(Info_Frame_Left, text="Member Type:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=0, column=0, sticky=W)
        Input_Member_Type = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthleft, textvariable=self.Member_Type).grid(row=0, column=1, sticky=W)

        Lbl_Member_ID = Label(Info_Frame_Left, text="Member ID:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=1, column=0, sticky=W)
        Input_Member_ID = ttk.Entry(Info_Frame_Left, font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthleft, textvariable=self.Member_ID)
        Input_Member_ID.grid(row=1, column=1, sticky=W)

        Input_Member_ID.bind('<KeyRelease>', Autofill)
        Input_Member_ID.bind("<Return>", lambda funct1: Input_Book_ID.focus())

        Lbl_First_Name = Label(Info_Frame_Left, text="First Name:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=2, column=0, sticky=W)
        Input_First_Name = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthleft, textvariable=self.First_Name).grid(row=2, column=1, sticky=W)

        Lbl_Last_Name = Label(Info_Frame_Left, text="Last Name:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=3, column=0, sticky=W)
        Input_Last_Name = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthleft, textvariable=self.Last_Name).grid(row=3, column=1, sticky=W)

        Lbl_Address = Label(Info_Frame_Left, text="Address:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=4, column=0, sticky=W)
        Input_Address = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthleft, textvariable=self.Address).grid(row=4, column=1, sticky=W)

        Lbl_Mail = Label(Info_Frame_Left, text="Mail ID:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=5, column=0, sticky=W)
        Input_Mail = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthleft, textvariable=self.Mail).grid(row=5, column=1, sticky=W)

        Lbl_PH = Label(Info_Frame_Left, text="Mobile Number:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=6, column=0, sticky=W)
        Input_PH = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthleft, textvariable=self.Ph).grid(row=6, column=1, sticky=W)

        Lbl_Cur_Amount = Label(Info_Frame_Left, text="Balance:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=7, column=0, sticky=W)
        Input_Cur_Amount = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthleft, textvariable=self.Cur_Amount).grid(row=7, column=1, sticky=W)

        # ----------- Label and Input Field for Right side of the Info_Frame_Left --------------- #

        Lbl_Book_ID = Label(Info_Frame_Left, text="Book ID:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=0, column=3, sticky=W)
        Input_Book_ID = ttk.Combobox(Info_Frame_Left, font=(
            "Comic Sans MS", fsize+yx, "bold"), width=ewidthright-xy, textvariable=self.Book_ID, cursor="hand2", state="readonly")

        Input_Book_ID.grid(row=0, column=4, sticky=W)
        Input_Book_ID.bind("<Return>", lambda funct1: Input_Book_ED.focus())

        Lbl_Book_Name = Label(Info_Frame_Left, text="Book Name:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=1, column=3, sticky=W)
        Input_Book_Name = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthright, textvariable=self.Book_Name).grid(row=1, column=4, sticky=W)

        Lbl_Book_ED = Label(Info_Frame_Left, text="Book Edition:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=2, column=3, sticky=W)
        Input_Book_ED = ttk.Spinbox(Info_Frame_Left,state="readonly", font=("Comic Sans MS", fsize, "bold"), width=ewidthright-1, textvariable=self.Book_ED, value=(
            "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th"), wrap=True)
        Input_Book_ED.grid(row=2, column=4, sticky=W)
        self.Book_ED.set("")
        Input_Book_ED.bind("<Return>", lambda funct1: Input_Due_Date.focus())

        Lbl_Book_Subject = Label(Info_Frame_Left, text="Book Subject:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=3, column=3, sticky=W)
        Input_Book_Subject = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthright, textvariable=self.Book_Subject).grid(row=3, column=4, sticky=W)

        Lbl_Author_Name = Label(Info_Frame_Left, text="Author Name:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=4, column=3, sticky=W)
        Input_Author_Name = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthright, textvariable=self.Author_Name).grid(row=4, column=4, sticky=W)

        Lbl_Shelf_NO = Label(Info_Frame_Left, text="Bookshelf No:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=5, column=3, sticky=W)
        Input_Due_Date = ttk.Entry(Info_Frame_Left, font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthright, state="readonly", textvariable=self.shelf_no)
        Input_Due_Date.grid(row=5, column=4, sticky=W)

        Lbl_Issue_Date = Label(Info_Frame_Left, text="Issue Date:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=6, column=3, sticky=W)
        Input_Issue_Date = ttk.Entry(Info_Frame_Left, state="readonly", font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthright, textvariable=self.Issue_Date).grid(row=6, column=4, sticky=W)

        Lbl_Due_Date = Label(Info_Frame_Left, text="Due Date:", font=(
            "Comic Sans MS", fsize, "bold"), padx=20, pady=py).grid(row=7, column=3, sticky=W)
        Input_Due_Date = ttk.Entry(Info_Frame_Left, font=(
            "Comic Sans MS", fsize, "bold"), width=ewidthright, textvariable=self.Due_Date)
        Input_Due_Date.grid(row=7, column=4, sticky=W)


## --------------------------------------- Info_Frame_Right -------------------------- ##

        Info_Frame_Right = LabelFrame(frame, text="Book Details",fg="#000716", bd=10, relief=RIDGE,
                                      font=("Comic Sans MS", 14, "bold"))
        #Info_Frame_Right_Right = LabelFrame(frame, relief=FLAT)

        # Screen Size Adjustment
        if wt > 1400:
            Info_Frame_Right.place(x=wt * (2 / 3) - 105,
                                   y=5, width=wt * 1 / 3 + 45, height=360)
            # Info_Frame_Right_Right.place(
            # x=wt * (2 / 3)+170, y=22, width=270, height=330)
            lbh = 8
            lbpy = 12
            blfs = 10
            fnt = 15
            lbw = 41  # 20
        else:
            Info_Frame_Right.place(x=wt * (2 / 3) - 105,
                                   y=5, width=wt * 1 / 3 + 45, height=305)
            # Info_Frame_Right_Right.place(
            # x=wt * (2 / 3)+170, y=22, width=215, height=278)
            lbh = 7
            lbpy = 6
            blfs = 5
            lbw = 36
            fnt = 14

        book_ScrollbarY = Scrollbar(Info_Frame_Right)
        book_ScrollbarY.grid(row=1, column=1, sticky=NS)

        book_ScrollbarX = Scrollbar(Info_Frame_Right, orient=HORIZONTAL)
        book_ScrollbarX.grid(row=2, column=0, sticky=EW)

        book_ListBox = Listbox(Info_Frame_Right, yscrollcommand=book_ScrollbarY.set,
                               xscrollcommand=book_ScrollbarX.set, font=("Comic Sans MS", fnt, "bold"), cursor="hand2", bd=2, width=lbw, height=lbh)
        book_ListBox.bind("<<ListboxSelect>>", Select_Book)
        book_ListBox.grid(row=1, column=0, padx=10, pady=lbpy)

        book_ScrollbarY.config(command=book_ListBox.yview)
        book_ScrollbarX.config(command=book_ListBox.xview)

        # display books name in book list box
        Display_Book()

        # Search Book Input
        entry = ttk.Entry(Info_Frame_Right, font=(
            "Comic Sans MS", 14, "bold"), width=lbw, textvariable=self.entry)
        entry.grid(row=0, column=0, padx=10)
        entry.bind('<KeyRelease>', Scankey)
        Update(book_list)


## ----------------------------------- Button Frame --------------------------------- ##

        Button_Frame = Frame(self.root, bd=10, relief=RIDGE, padx=2, pady=3)
        # Button Size Adjustment.
        if wt > 1400:
            Button_Frame.place(x=0, y=510, width=wt, height=70)
            bw = 20
            pa = 2
            pb = 3
            pc = 2

        else:
            Button_Frame.place(x=0, y=455, width=wt, height=60)
            bw = 21
            pa = 2
            pb = 3
            pc = 3

        # Button Input #

        Btn_Add_Data = Button(Button_Frame, text="Issue Book", font=("Comic Sans MS", fsize, "bold"), cursor="hand2", width=bw, bg="#000716",
                              fg="white", padx=pa, command=Add_Data).grid(row=0, column=0)
        Btn_Clear_Data = Button(Button_Frame, command=Clear_Data, text="Clear", font=("Comic Sans MS", fsize, "bold"), cursor="hand2", width=bw, bg="#000716",
                                fg="white", padx=pb).grid(row=0, column=1)
        Btn_Add_Member = Button(Button_Frame, text="Add Member", font=("Comic Sans MS", fsize, "bold"), cursor="hand2", width=bw, bg="#000716",
                                fg="white", padx=pb, command=Add_Member_btn_f).grid(row=0, column=2)
        Btn_Add_Book = Button(Button_Frame, command=Add_Book_btn_f, text="Add Book", font=("Comic Sans MS", fsize, "bold"), cursor="hand2", width=bw, bg="#000716",
                              fg="white", padx=pc).grid(row=0, column=3)
        Btn_Return_Book = Button(Button_Frame, text="Return Book", font=("Comic Sans MS", fsize, "bold"), cursor="hand2", width=bw, bg="#000716",
                                 fg="white", padx=pc, command=Return_Book_btn_f).grid(row=0, column=4)
        Btn_Exit_Data = Button(Button_Frame, command=Qt_Win, text="Exit", font=("Comic Sans MS", fsize, "bold"), cursor="hand2", width=bw,
                               bg="#000716", fg="white", padx=pa).grid(row=0, column=5)


## ----------------------------------Database Frame & Table Frame --------------------------------- ##

        DatabaseFrame = Frame(self.root, bd=10, relief=RIDGE, padx=10)
        Table_Frame = Frame(DatabaseFrame, bd=6, relief=RIDGE, padx=0, pady=0)
        if wt > 1400:
            DatabaseFrame.place(x=0, y=585, width=wt, height=230)
            Table_Frame.place(x=0, y=5, width=wt-40, height=200)
        else:
            DatabaseFrame.place(x=0, y=520, relwidth=1, height=200)
            Table_Frame.place(x=0, y=5, width=wt-40, height=170)

        Xscroll = Scrollbar(Table_Frame, orient=HORIZONTAL)
        Yscroll = Scrollbar(Table_Frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_Frame, column=("sr_no", "refno", "mtype", "mid", "mfname", "mlname", "madd", "mmail", "mmob",
                                          "bid", "bname", "bed", "bsub", "bauth", "bshelf", "bissu", "bdue", "bretdate", "curamount"), xscrollcommand=Xscroll.set, yscrollcommand=Yscroll.set)

        Xscroll.pack(side=BOTTOM, fill=X)
        Yscroll.pack(side=RIGHT, fill=Y)

        Xscroll.config(command=self.library_table.xview)
        Yscroll.config(command=self.library_table.yview)

        self.library_table.heading("sr_no", text="Serial No")
        self.library_table.heading("refno", text="Reference No")
        self.library_table.heading("mtype", text="Member Type")
        self.library_table.heading("mid", text="Member Id")
        self.library_table.heading("mfname", text="First Name")
        self.library_table.heading("mlname", text="Last Name")
        self.library_table.heading("madd", text="Address")
        self.library_table.heading("mmail", text="Mail Id")
        self.library_table.heading("mmob", text="Mobile No")
        self.library_table.heading("bid", text="Book Id")
        self.library_table.heading("bname", text="Book Name")
        self.library_table.heading("bed", text="Book Edition")
        self.library_table.heading("bsub", text="Book Subject")
        self.library_table.heading("bauth", text="Book Author")
        self.library_table.heading("bshelf", text="Bookshelf No")
        self.library_table.heading("bissu", text="Issue Date")
        self.library_table.heading("bdue", text="Due Date")
        self.library_table.heading("bretdate", text="Returned Date")
        self.library_table.heading("curamount", text="Current Balance")

        self.library_table.column("sr_no", width=100, stretch=0, anchor=CENTER)
        self.library_table.column("refno", width=150, stretch=0, anchor=CENTER)
        self.library_table.column("mtype", width=140, stretch=0, anchor=CENTER)
        self.library_table.column("mid", width=150, stretch=0, anchor=CENTER)
        self.library_table.column(
            "mfname", width=150, stretch=0, anchor=CENTER)
        self.library_table.column(
            "mlname", width=150, stretch=0, anchor=CENTER)
        self.library_table.column("madd", width=200, stretch=0, anchor=CENTER)
        self.library_table.column("mmail", width=200, stretch=0, anchor=CENTER)
        self.library_table.column("mmob", width=150, stretch=0, anchor=CENTER)
        self.library_table.column("bid", width=150, stretch=0, anchor=CENTER)
        self.library_table.column("bname", width=200, stretch=0, anchor=CENTER)
        self.library_table.column("bed", width=100, stretch=0, anchor=CENTER)
        self.library_table.column("bsub", width=100, stretch=0, anchor=CENTER)
        self.library_table.column("bauth", width=150, stretch=0, anchor=CENTER)
        self.library_table.column(
            "bshelf", width=100, stretch=0, anchor=CENTER)
        self.library_table.column("bissu", width=100, stretch=0, anchor=CENTER)
        self.library_table.column("bdue", width=100, stretch=0, anchor=CENTER)
        self.library_table.column(
            "bretdate", width=100, stretch=0, anchor=CENTER)
        self.library_table.column(
            "curamount", width=100, stretch=0, anchor=CENTER)

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)
        self.library_table.bind("<ButtonRelease-1>", Get_Cursor)
        Lbl_footer = Label(self.root,text="Developed By Department of Computer Science, Syamaprasad College.",font=("Comic Sans MS", 13, "bold"),bg="#000716",fg="#f1f1f1")
        
        if wt > 1400:
             Lbl_footer.place(x=0,y=815,relwidth=1,height=30)
        else:
            Lbl_footer.place(x=0,y=720,relwidth=1,height=30)
        Display_Data()

## -------------------------------- TTK Customization ---------------------------------- ##
        style1 = ttk.Style()
        style1.configure('TEntry', background='black')
        style1.configure('TSpinbox', background='black',
                         selectbackground='none', selectforeground='black')
        style1.configure('TCombobox', background='black')
        style1.configure('Treeview', font=("Comic Sans MS", 10))
        style1.configure('Treeview.Heading', font=(
            "Comic Sans MS", 10, "bold"))
