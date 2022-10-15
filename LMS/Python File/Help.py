from tkinter import *
from tkinter import ttk

class Help_Class:

    def __init__(self):


        def Select_items(items=""):
            textbox['state']='normal' 
            value = str(listbox.get((listbox.curselection()))) 
                      
            textbox.delete("1.0",END)
            
            if value=="Shortcuts":
                Fact="----------- Shortcut Keys ----------\n\nMinimize---> F11\nExit---> Ctrl+Q\nRefresh---> Esc\nAdd Member---> Ctrl+M\nDelete Record---> Ctrl+D\nHelp---> F1"
            elif value=="Add Member":
                Fact="---------- How to Add Member ---------\n\nStep 1: Cick on 'Add Member' button.\nStep 2: Fill up the necessary details.\nStep 3: Click on 'Generate Member Id'\n          button."
            elif value=="Modify Member":
                Fact="----- How to Modify Member Details ----\n\nStep 1: Cick on 'Edit' button.\nStep 2: Cick on 'Modify Member' button.\nStep 3: Fill up the necessary details.\nStep 4: Click on 'Update Member Details'\n          button."    
            elif value=="Add Book":
                Fact="------------ How to Add Book ----------\n\nStep 1: Cick on 'Add Book' button.\nStep 2: Fill up the necessary details.\nStep 3: Click on 'Submit' button."
            elif value=="Issue Book":
                Fact="---------- How to Issue a Book --------\n\nStep 1: Write the member id in the entry\n         field.\nStep 2: Select the book from book  details.\nStep 3: Fill up the rest necessary details.\nStep 4: Click on 'Issue Book' button."
            elif value=="Return Book":
                Fact="---------- How to Return a Book -------\n\nStep 1: Cick on 'Return  Book' button.\nStep 2: Fill up the necessary details.\nStep 3: Click on 'Submit' button."
            elif value=="Lost Book":
                Fact="------- Report Lost Book Details -------\n\nStep 1: Cick on 'Edit' button.\nStep 2: Cick on 'Modify Book' button.\nStep 3: Cick on 'Lost Book' button.\nStep 4: Fill up the necessary details.\nStep 5: Click on 'Submit' button."
            elif value=="Update Book":
                Fact="---------- Update Book Details ---------\n\nStep 1: Cick on 'Edit' button.\nStep 2: Cick on 'Modify Book' button.\nStep 3: Cick on 'Update Book Details' button.\nStep 4: Fill up the necessary details.\nStep 5: Click on 'Submit' button."        


            textbox.insert(END, Fact)
            textbox['state']='disable' 


        top = Toplevel()
        top.grab_set()
        top.focus_force()

        top.title("Library Management System | Help")

        app_width = 800
        app_height = 380

        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y-13)}')
        top.resizable(False, False)
        top.iconbitmap('icon.ico')

        LBL_HD=Label(top,font=("Comic Sans MS", 20, "bold"),text="How May I Help you ?").pack(pady=20)
        
        frame1 = Frame(top,relief=RIDGE,bd=12)
        frame1.place(x=10, y=80, width=510, height=270)
        textbox=Text(frame1,font=("Comic Sans MS", 16, "bold"),height=8,width=37,state="disable")
        textbox.grid(row=0,column=0)
        
        frame2 = Frame(top,relief=RIDGE,bd=12)
        frame2.place(x=530, y=80, width=250, height=270)
        listbox = Listbox(frame2,font=("Comic Sans MS", 14, "bold"),height=8,width=18)
        listbox.grid(row=0,column=0,padx=2,pady=8)
        listbox.bind("<<ListboxSelect>>", Select_items)
        

        lst=["Shortcuts","Add Member","Modify Member","Add Book","Issue Book","Return Book","Lost Book","Update Book"]

        for item in lst:
            listbox.insert(END,item)
        
        top.mainloop()