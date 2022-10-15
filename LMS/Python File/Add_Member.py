from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import re
import smtplib,ssl
import random,string

class Add_Member_Class:

    def __init__(self, username, dbpassword):

        def Clear():
            self.M_Type.set("")
            self.F_Name.set("")
            self.L_Name.set("")
            self.Add.set("")
            self.Dept.set("")
            self.Ml.set("")
            self.Phone.set("")
            self.C_Amount.set("")
            self.St.set("")

        def Btn_Add_M():
            if self.M_Type.get() == "" or self.F_Name.get() == "" or self.L_Name.get() == "" or self.Add.get() == "" or self.St.get()=="" or self.Dept.get() == "" or self.Ml.get() == "" or self.Phone.get() == "" or self.C_Amount.get() == "":
                messagebox.showerror(
                    'Library Management System', 'Please Fill All The Fields.', parent=top)
                return
            
            if self.F_Name.get().replace(' ','').isalpha():
                if self.L_Name.get().replace(' ','').isalpha():
                    if self.C_Amount.get().isnumeric() and int(self.C_Amount.get()) >=1 and int(self.C_Amount.get())<=100000:
                        if self.Phone.get().isnumeric():
                            if len(self.Phone.get())==10:
                                if re.fullmatch(regex, self.Ml.get()):
                                    try:
                                        sqlCon = pymysql.connect(
                                            host="localhost", user=username, password=dbpassword, database="lms")
                                        cur = sqlCon.cursor()
                                        
                                        result_str = ''.join(random.choice(string.ascii_letters) for i in range(8))
                                        
                                        pw.set(result_str)

                                        cur.execute("insert into member_details (member_type,first_name,last_name,address,dept,mail,mobile,amount,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);", (self.M_Type.get(
                                        ).title(), self.F_Name.get().title(), self.L_Name.get().title(), self.Add.get().title(), self.St.get()+" "+self.Dept.get(), self.Ml.get(), self.Phone.get(), self.C_Amount.get(),pw.get()))

                                        cur.execute(
                                            "select member_id from member_details where mobile=%s;", (self.Phone.get()))
                                        result = cur.fetchall()
                                        if len(result) != 0:
                                            for row in result:
                                                self.M_Id.set(row[0])

                                        sqlCon.commit()
                                        sqlCon.close()

                                
                                        try:
                                            Phone=self.Phone.get()
                                            Phone=Phone[0:3]+"XXXX"+Phone[7:10]
                                            port = 587  # For SSL
                                            host = "smtp-mail.outlook.com"
                                            sender_email = "librarymanagementsystemproject@outlook.com"  # Enter your address
                                            receiver_email = self.Ml.get() # Enter receiver address
                                            password = "lms@1234"

                                            subject="Membership Registration Confirmation"
                                            body="Congratulations! You have been registered successfully on Our Library Management System.\n\nMembership Information:\n\nMember Type : "+self.M_Type.get().title()+" \nFirst Name : "+self.F_Name.get().title()+" \nLast Name : "+self.L_Name.get().title()+" \nAddress : "+self.Add.get().title()+" \nDepartment : "+self.St.get()+" "+self.Dept.get()+"\nMail ID : "+self.Ml.get()+" \nMobile No : "+Phone+" \nDeposit Amount : "+self.C_Amount.get()+" \n\n\nYour Member Id/Username is : "+self.M_Id.get()+" \nYour password is : "+pw.get()+" \n\n\nThank You."

                                            message = f'Subject: {subject}\n\n{body}'

                                            server = smtplib.SMTP(host, port)
                                            server.starttls()
                                            server.login(sender_email, password)
                                            output = server.sendmail(sender_email, receiver_email, message)

                                        except:
                                            pass

                                        finally:
                                            messagebox.showinfo(
                                                'Library Management System', 'Member Registration Successfully\n\nThe Member Id Is : '+self.M_Id.get(), parent=top)
                                            Clear()
                                            self.M_Id.set("")
                                    except:
                                        cur.execute(
                                            "select max(`member_id`)+1 from member_details;")
                                        result = cur.fetchall()
                                        if len(result) != 0:
                                            for row in result:
                                                val = row[0]
                                        cur.execute(
                                            "ALTER TABLE `member_details` auto_increment =%s;", (val))

                                        sqlCon.commit()
                                        sqlCon.close()
                                        messagebox.showerror(
                                            'Library Management System', 'Member Already Exist.\nPlease check again or go to Forget Member Id.', parent=top)
                                else:
                                    messagebox.showerror(
                                        'Library Management System', 'Mail Id Like "simple@example.com" ', parent=top)

                            else:
                                messagebox.showerror(
                                    'Library Management System', 'Length of Phone Numbers Must be 10', parent=top)
                        else:
                            messagebox.showerror(
                                'Library Management System', 'Phone Number Do not Contain Any Charecter Or Special Charecter', parent=top)

                    else:
                        messagebox.showerror(
                            'Library Management System', 'Deposit Amount Do not Contain Any Charecters Or Special Charecters.\n\t\tAnd\n\n1 >= Deposite Amount <= 1,00,000', parent=top)

                else:
                    messagebox.showerror(
                        'Library Management System', 'Last Name Do not Contain Any Numbers Or Special Charecter', parent=top)

            else:
                messagebox.showerror(
                    'Library Management System', 'First Name Do not Contain Any Numbers Or Special Charecter', parent=top)
        
        
        def Deptselect(event=""):
            self.Dept.set("")

            if self.St.get()=="B.Sc":
                Input_Dept['value'] = ["Computer Science","Mathematics","Physics","Geography","Electronics","Economics","Biological Science","Others"]
            elif self.St.get()=="B.Com":
                Input_Dept['value'] = ["Commerce","Others"]
            elif self.St.get()=="Other":
                Input_Dept['value'] = ["Office Staff"]
            else:
                Input_Dept['value'] = ["Bengali","English","French","Hindi","Philosophy","Education","History","Political Science","Sanskrit","Others"]
        
        self.M_Type = StringVar()
        self.M_Id = StringVar()
        self.F_Name = StringVar()
        self.L_Name = StringVar()
        self.Add = StringVar()
        self.Dept = StringVar()
        self.St=StringVar()
        self.Ml = StringVar()
        self.Phone = StringVar()
        self.C_Amount = StringVar()
        pw=StringVar()
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        top = Toplevel()
        top.grab_set()

        top.title("Library Management System | Member Registration")
        Clear()

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

        dmylbl = Label(frame, font=("Comic Sans MS", 8, "bold")).grid(row=0, column=0)

        Lbl_Member_Type = Label(frame, text="Member Type:", font=(
            "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=1, column=0, sticky=W)

        Input_Member_Type = ttk.Combobox(frame,width=20, font=(
            "Comic Sans MS", 20, "bold"), cursor="hand2", state="readonly", textvariable=self.M_Type)
        Input_Member_Type['value'] = ("Student","Teacher","Staff")
        Input_Member_Type.grid(row=1, column=1, sticky=W)
        Input_Member_Type.bind(
            "<Return>", lambda funct1: Input_First_Name.focus())
        Input_Member_Type.focus()

        Lbl_First_Name = Label(frame, text="First Name:", font=(
            "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=2, column=0, sticky=W)

        Input_First_Name = ttk.Entry(frame,width=21, font=(
            "Comic Sans MS", 20, "bold"), textvariable=self.F_Name)
        Input_First_Name.grid(row=2, column=1, sticky=W)
        Input_First_Name.bind(
            "<Return>", lambda funct1: Input_Last_Name.focus())

        Lbl_Last_Name = Label(frame, text="Last Name:", font=(
            "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=3, column=0, sticky=W)

        Input_Last_Name = ttk.Entry(frame,width=21, font=(
            "Comic Sans MS", 20, "bold"), textvariable=self.L_Name)
        Input_Last_Name.grid(row=3, column=1, sticky=W)
        Input_Last_Name.bind("<Return>", lambda funct1: Input_Address.focus())

        Lbl_Address = Label(frame, text="Address:", font=(
            "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=4, column=0, sticky=W)

        Input_Address = ttk.Entry(frame,width=21, font=(
            "Comic Sans MS", 20, "bold"), textvariable=self.Add)
        Input_Address.grid(row=4, column=1, sticky=W)
        Input_Address.bind("<Return>", lambda funct1: Input_St.focus())

        Lbl_Dept = Label(frame, text="Department:", font=(
            "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=5, column=0, sticky=W)

        Input_St = ttk.Combobox(frame, font=(
            "Comic Sans MS", 18, "bold"), width=5, cursor="hand2", state="readonly", textvariable=self.St)
        Input_St.grid(row=5, column=1, sticky=W)
        Input_St['value']=["B.Sc","B.Com","B.A","Other"]
        Input_St.bind('<<ComboboxSelected>>', Deptselect)
        Input_St.bind("<Return>", lambda funct1: Input_Dept.focus())

        Input_Dept = ttk.Combobox(frame, font=(
            "Comic Sans MS", 18, "bold"), width=14, cursor="hand2", state="readonly", textvariable=self.Dept)
        
        Input_Dept.grid(row=5, column=1, sticky=W,padx=110)
        Input_Dept.bind("<Return>", lambda funct1: Input_Mail.focus())

        Lbl_Mail = Label(frame, text="Mail ID:", font=(
            "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=6, column=0, sticky=W)

        Input_Mail = ttk.Entry(frame, font=(
            "Comic Sans MS", 20, "bold"),width=21, textvariable=self.Ml)
        Input_Mail.grid(row=6, column=1, sticky=W)
        Input_Mail.bind("<Return>", lambda funct1: Input_PH.focus())

        Lbl_PH = Label(frame, text="Mobile Number:", font=(
            "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=7, column=0, sticky=W)

        Input_PH = ttk.Entry(frame,width=21, font=(
            "Comic Sans MS", 20, "bold"), textvariable=self.Phone)
        Input_PH.grid(row=7, column=1, sticky=W)
        Input_PH.bind("<Return>", lambda funct1: Input_Cur_Amount.focus())

        Lbl_Cur_Amount = Label(frame, text="Deposit:", font=(
            "Comic Sans MS", 20, "bold"), padx=80, pady=10).grid(row=8, column=0, sticky=W)

        Input_Cur_Amount = ttk.Entry(frame,width=21, font=(
            "Comic Sans MS", 20, "bold"), textvariable=self.C_Amount)
        Input_Cur_Amount.grid(row=8, column=1, sticky=W)

        Btn_Add_Member = Button(frame, text="Generate Member Id", width=20, bg="#000716", cursor="hand2", fg="white", font=(
            "Comic Sans MS", 15, "bold"), command=Btn_Add_M).place(x=300, y=530)
