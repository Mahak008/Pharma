from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk # pip install pillow
from tkinter import messagebox
import mysql.connector

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        
        #Login window geometry
        self.root.geometry('1500x800+0+0')
        #=====================addMed variable==========================
        self.addmed_var=StringVar()
        self.refMed_var=StringVar()

        #=============main variable===================
        self.ref_var=StringVar()
        self.cmpname_var=StringVar()
        self.typMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideeffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Mahak\OneDrive\Desktop\Python Website\background.jpg")
        
        # Label of background img
        lbl_bg = Label(self.root, image=self.bg)

        #Placing the background img
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame of background image
        frame = Frame(self.root, bg="black")
        frame.place(x=500, y=140, width=340, height=450)

        #Login icon image
        img1 = Image.open(r"C:\Users\Mahak\OneDrive\Desktop\Python Website\icon.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Label of Login icon
        lblimg1 = Label(image = self.photoimg1, bg="white", borderwidth=0)
        lblimg1.place(x=623, y=100, width=100, height=100)

        # Label for get started
        get_str = Label(frame, text="Get Started", font=("Times New Roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=100, y=80)

        # Label for username
        username = lbl = Label(frame, text="Username", font=("Times New Roman", 14, "bold"), fg="white", bg="black")
        username.place(x=40, y=140)
        self.txtuser = ttk.Entry(frame, font=("Times New Roman", 14, "bold"))
        self.txtuser.place(x=43, y=170, width=255)

        # Label for password
        password = lbl = Label(frame, text="Password", font=("Times New Roman", 14, "bold"), fg="white", bg="black")
        password.place(x=40, y=220)
        self.txtpass = Entry(frame, font=("Times New Roman", 14, "bold"))
        self.txtpass.place(x=43, y=250, width=255)

        # Login Button
        loginbtn = Button(frame, command=self.login, text="Login", font=("Times New Roman", 16, "bold"), bd=3, relief=RIDGE, fg="white", bg="black", activebackground="black", activeforeground="white")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register Button
        regbtn = Button(frame, text="New User? Register", command=self.register_window, font=("Times New Roman", 10, "bold"), borderwidth=0, bg="black", fg="white", activebackground="black", activeforeground="white")
        regbtn.place(x=40, y=360, width=120)

        # Forgot Button
        forbtn = Button(frame, text="Forgot Password", command=self.forgot_pass_win, font=("Times New Roman", 10, "bold"),  borderwidth=0, bg="black", fg="white", activebackground="black", activeforeground="white")
        forbtn.place(x=30, y=380, width=120)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")

        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome User!")

        else :
            # connect database
            conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email = %s AND pass = %s", (
                self.txtuser.get(), self.txtpass.get()
            ))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username or Password.")
            else :
                open_main = messagebox.askyesno("YesNo", "Access only admin.")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = PharmacyManagementSystem(self.new_window)
                else :
                    if not open_main:
                        return
                
            conn.commit()
            conn.close()

    # Reset Password
    def reset_pass(self):
        if self.combo_sec.get() == "Select":
            messagebox.showerror("Error", "Select the security question", parent = self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent = self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent = self.root2)
        else:
            # connect database
            conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email = %s AND sec_q = %s AND sec_ans = %s")
            value = (self.txtuser.get(), self.combo_sec.get(), self.txt_security.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error", "Please enter the correct answer", parent = self.root2)

            else :
                query = ("UPDATE register SET pass = %s WHERE email = %s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password is reset.", parent = self.root2)

                self.root2.destroy()

    # Forgot Password
    def forgot_pass_win(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email.")
        else :
            conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email = %s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("Error", "Please enter the valid username")
            else :
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("350x450+500+160")

                l = Label(self.root2, text="Forgot Password", font=("Times New Roman", 14, "bold"),  bg="black", fg="white")
                l.place(x=0, y=10, relwidth=1)

                sec_ques = Label(self.root2, text="Select Security Question", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
                sec_ques.place(x=50, y=80)
                self.combo_sec = ttk.Combobox(self.root2, font=("Times New Roman", 14, "bold"), state="readonly")
                self.combo_sec["values"] = ("Select","Your Birthplace", "Your City", "Your Pet Name", "Your School Name")
                self.combo_sec.place(x=50, y=110, width=250)
                self.combo_sec.current(0);

                sec_ans = Label(self.root2, text="Security Answer", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
                sec_ans.place(x=50, y=150)
                self.sec_ans_entry = ttk.Entry(self.root2, font=("Times New Roman", 14, "bold"))
                self.sec_ans_entry.place(x=50, y=180, width=250)

                new_pass = Label(self.root2, text="New Password", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
                new_pass.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("Times New Roman", 14, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)     

                btn = Button(self.root2, text = "Reset", command=self.reset_pass, font=("Times New Roman", 14, "bold"),fg="white", bg="black")           
                btn.place(x=90, y= 300, width= 150)

class Register :
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        
        #Login window geometry
        self.root.geometry('1550x800+0+0')
        
        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_sec_ques = StringVar()
        self.var_sec_ans = StringVar()
        self.var_pass = StringVar()
        self.var_cpass = StringVar()
        self.var_check = IntVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Mahak\OneDrive\Desktop\Python Website\background.jpg")
        
        # Label of background img
        lbl_bg = Label(self.root, image=self.bg)

        #Placing the background img
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame of background image
        frame = Frame(self.root, bg="white")
        frame.place(x=285, y=100, width=800, height=520)

        # Register label
        reg_lbl = Label(frame, text="Register Here", font=("Times New Roman", 20, "bold"), fg="black", bg="white")
        reg_lbl.place(x=310, y=35)

        # Entry Fields
        fname = Label(frame, text="First Name", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("Times New Roman", 14, "bold"))
        fname_entry.place(x=50, y=130, width=300)

        lname = Label(frame, text="Last Name", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
        lname.place(x=450, y=100)
        self.lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("Times New Roman", 14, "bold"))
        self.lname_entry.place(x=450, y=130, width=300)

        contact = Label(frame, text="Contact No.", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
        contact.place(x=50, y=180)
        self.contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("Times New Roman", 14, "bold"))
        self.contact_entry.place(x=50, y=210, width=300)

        email = Label(frame, text="Email", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
        email.place(x=450, y=180)
        self.email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("Times New Roman", 14, "bold"))
        self.email_entry.place(x=450, y=210, width=300)

        sec_ques = Label(frame, text="Select Security Question", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
        sec_ques.place(x=50, y=260)
        self.combo_sec = ttk.Combobox(frame, textvariable=self.var_sec_ques, font=("Times New Roman", 14, "bold"), state="readonly")
        self.combo_sec["values"] = ("Select","Your Birthplace", "Your City", "Your Pet Name", "Your School Name")
        self.combo_sec.place(x=50, y=290, width=300)
        self.combo_sec.current(0);

        sec_ans = Label(frame, text="Security Answer", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
        sec_ans.place(x=450, y=260)
        self.sec_ans_entry = ttk.Entry(frame, textvariable=self.var_sec_ans, font=("Times New Roman", 14, "bold"))
        self.sec_ans_entry.place(x=450, y=290, width=300)

        password = Label(frame, text="Password", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
        password.place(x=50, y=340)
        self.password_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("Times New Roman", 14, "bold"))
        self.password_entry.place(x=50, y=370, width=300)

        c_pass = Label(frame, text="Confirm Password", font=("Times New Roman", 16, "bold"), fg="black", bg="white")
        c_pass.place(x=450, y=340)
        self.c_pass_entry = ttk.Entry(frame, textvariable=self.var_cpass, font=("Times New Roman", 14, "bold"))
        self.c_pass_entry.place(x=450, y=370, width=300) 

        # Check Button
        check_btn = Checkbutton(frame, variable=self.var_check, text="I Agree to the Terms and Conditions given.", font=("Times New Roman", 12, "bold"), onvalue=1, offvalue=0)
        check_btn.place(x=130, y=420, width=500)

        # Register button
        regbtn = Button(frame, text="Register", command=self.register_data, font=("Times New Roman", 16, "bold"), bd=3, relief=RIDGE, fg="white", bg="black", activebackground="black", activeforeground="white")
        regbtn.place(x=240, y=460, width=120, height=35)

        # Login Button
        loginbtn = Button(frame, text="Login", command=self.return_login, font=("Times New Roman", 16, "bold"), bd=3, relief=RIDGE, fg="white", bg="black", activebackground="black", activeforeground="white")
        loginbtn.place(x=430, y=460, width=120, height=35)

    # Register button functionality
    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_email.get() == "" or self.var_sec_ques.get() == "Select" or self.var_sec_ans.get() == "":
            messagebox.showerror("Error", "All fields are required.")
        elif self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error", "Password do not match.")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Kindly agree the terms & conditions.")
        else :
            # connext database
            conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
            my_cursor = conn.cursor()
            query = ("SELECT * from register WHERE email = %s")
            
            # fetch the data of email field
            value = (self.var_email.get(), )

            # execute query
            my_cursor.execute(query, value)
            row = my_cursor.fetchone() # fetch only one row
            if row != None:
                messagebox.showerror("Error", "User already exists. Try with another email.")
            else :
                my_cursor.execute("INSERT INTO register VALUES(%s, %s, %s, %s, %s, %s, %s)", (self.var_fname.get(), self.var_lname.get(), self.var_contact.get(), self.var_email.get(), self.var_sec_ques.get(), self.var_sec_ans.get(), self.var_pass.get()))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully.")

    def return_login(self):
        self.root.destroy()

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

    #=====================Add Medicine variable===================
        self.refMed_var=StringVar()
        self.addmed_var=StringVar()

    # ===================Main Variables===========================
        self.ref_var = StringVar()
        self.cmpname_var = StringVar()
        self.typeMed_var = StringVar()
        self.medName_var = StringVar()
        self.lot_var = StringVar()
        self.issuedate_var = StringVar()
        self.expdate_var = StringVar()
        self.uses_var = StringVar()
        self.sideeffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.product_var = StringVar()

        lbltitle=Label(self.root,text="Pharamacy Management System", bd=15, relief=RIDGE, bg='white',fg="darkgreen", font=("times new roman",50,"bold"), padx=2, pady=4)
        
        lbltitle.pack(side=TOP,fill=X)

        # img1=Image.open("python/logo.jpg")
        # img1 = img1.resize((80, 80))
        # self.photoimg1=ImageTk.PhotoImage(img1)
        # b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        # b1.place(x=70,y=20)
        
        #==================DataFrame=====================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1350,height=400)

        DataFramerLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                 fg="darkgreen",font=("arial",12,"bold"))
        DataFramerLeft.place(x=0,y=5,width=910,height=350)

        DataFramerRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                 fg="darkgreen",font=("arial",12,"bold"))
        DataFramerRight.place(x=910,y=5,width=380,height=350)

        

        #==================ButtonsFrame========================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1350,height=65)

        #=================MainButton===========================
        btnAddData=Button(ButtonFrame, command=self.add_data, text="Medicine Add",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnUpdateMed=Button(ButtonFrame, text="Update", font=("arial",13, "bold"), width = 12, bg="darkgreen", fg="white")
        btnUpdateMed .grid (row=0,column=1)

        btnDeleteData=Button(ButtonFrame,text="Delete",font=("arial",13,"bold"), width = 12, bg="red",fg="white")
        btnDeleteData.grid(row=0,column=2)

        btnResetData=Button(ButtonFrame,text="Reset",font=("arial",13,"bold"), width = 12, bg="darkgreen",fg="white")
        btnResetData.grid(row=0,column=3)

        btnExitData=Button(ButtonFrame,text="Exit",font=("arial",13,"bold"), width = 12, bg="darkgreen",fg="white")
        btnExitData.grid(row=0,column=4)

        #================Search by============================
        lblSearch=Label(ButtonFrame,font=("arial",13,"bold"),text="Search by", width = 12, bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)
        
        serch_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",13,"bold"),state="readonly")
        serch_combo["values"]=("Ref","Medname","Lot")
        serch_combo.grid(row=0,column=6)
        serch_combo.current(0)

        txtSerch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("arial",13,"bold"))
        txtSerch.grid(row=0,column=7)

        serchBtn=Button(ButtonFrame,text="SEARCH",font=("arial",13,"bold"),width=12,bg="darkgreen",fg="white")
        serchBtn.grid(row=0,column=8)
        
        showAll=Button(ButtonFrame,text="SHOW ALL",font=("arial",13,"bold"),width=12,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)


        #========================Lables and Entry==========================
        lblrefno=Label(DataFramerLeft, font=("arial",12, "bold"), text="Reference No", padx=2, pady=6)
        lblrefno.grid (row=0, column=0, sticky=W )
        
        conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
        my_cursor=conn.cursor() 
        my_cursor.execute("SELECT ref FROM pharma")
        row = my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataFramerLeft, textvariable=self.ref_var, width=27,font=("arial",12,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        # ref_combo.current(0)

        lblCmpName=Label(DataFramerLeft, font=("arial",12,"bold"),text="Company Name:",padx=2,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFramerLeft, textvariable=self.cmpname_var, font=("arial",13,"bold"),bd=2,relief=RIDGE,width=29)
        txtCmpName.grid(row=1,column=1)
        
        lblTypeofMedicine=Label(DataFramerLeft, font=("arial",12,"bold"),text="Type of Medicine:",padx=2,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFramerLeft, textvariable=self.typeMed_var, state="readonly",
                                     font=("arial",12,"bold"),width=27)
        comTypeofMedicine['value']=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injections",)
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2,column=1)


        #===================Add Medicine==============================

        conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
        my_cursor=conn.cursor() 
        my_cursor.execute("SELECT med_name FROM pharma")
        med = my_cursor.fetchall()

        lblMedicineName=Label(DataFramerLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)
        
        comMedicineName=ttk.Combobox(DataFramerLeft,state="readonly",
                                     font=("arial",12,"bold"),width=27)
        comMedicineName['value']=("nice","novel")
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)
        
        lblLotNo=Label(DataFramerLeft,font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFramerLeft,textvariable=self.lot_var, font=("arial",13,"bold"),bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)
        
        
        lblIssueDate=Label(DataFramerLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFramerLeft, textvariable=self.issuedate_var, font=("arial",13,"bold"),bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)
        
        lblExDate=Label(DataFramerLeft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFramerLeft, textvariable=self.expdate_var,font=("arial",13,"bold"),bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1)
        
        lblUses=Label(DataFramerLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFramerLeft, textvariable=self.uses_var,font=("arial",13,"bold"),bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)
        
        
        lblSideEffect=Label(DataFramerLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFramerLeft,font=("arial",13,"bold"),textvariable=self.sideeffect_var,bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)
        
        lblPreWarning=Label(DataFramerLeft,font=("arial",12,"bold"),text="Prec&Warning:",padx=2,pady=6)
        lblPreWarning.grid(row=0,column=2,sticky=W)
        txtPreWarning=Entry(DataFramerLeft,font=("arial",13,"bold"),textvariable=self.warning_var,bd=2,relief=RIDGE,width=29)
        txtPreWarning.grid(row=0,column=3)
        
        
        lblDosage=Label(DataFramerLeft,font=("arial",12,"bold"),text="Dosage:",padx=2,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFramerLeft,font=("arial",13,"bold"), textvariable=self.dosage_var,bd=2,relief=RIDGE,width=29)
        txtDosage.grid(row=1,column=3)
        
        
        lblPrice=Label(DataFramerLeft,font=("arial",12,"bold"),text="Tablets Price:",padx=2,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFramerLeft,font=("arial",13,"bold"),textvariable=self.price_var,bd=2,relief=RIDGE,width=29)
        txtPrice.grid(row=2,column=3)
        
        
        lblProductQt=Label(DataFramerLeft,font=("arial",12,"bold"),text="Product QT:",padx=2,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W )
        txtProductQt=Entry(DataFramerLeft,font=("arial",13,"bold"),textvariable=self.product_var,bd=2,relief=RIDGE,width=29)
        txtProductQt.grid(row=3,column=3,sticky=W)

        #=====================Images==========================
        lblhome=Label(DataFramerLeft,font=("arial",12,"bold"),text="Stay Home Stay Safe",padx=2,pady=6,fg="red",width=37  )
        lblhome.place(x=500,y=140)

        # img2=Image.open("python/img4.jpg")
        # img2 = img2.resize((150, 135))
        # self.photoimg2=ImageTk.PhotoImage(img2)
        # b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        # b1.place(x=770,y=330)

        # img3=Image.open("python/img5.jpg")
        # img3 = img3.resize((150, 135))
        # self.photoimg3=ImageTk.PhotoImage(img3)
        # b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        # b1.place(x=620,y=330)

        # img4=Image.open("python/images.jpeg")
        # img4 = img4.resize((150, 135))
        # self.photoimg4=ImageTk.PhotoImage(img4)
        # b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        # b1.place(x=475,y=330)

       #====================DataFrameRight=====================
       
        DataFramerRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department ",
                                   fg="darkgreen",font=("arial",12,"bold"))
        DataFramerRight.place(x=910,y=5,width=540,height=350)

        # img5=Image.open("python/img2.jpg")
        # img5=img5. resize((200,75))
        # self. photoimg5=ImageTk. PhotoImage (img5)
        # b1=Button(self.root, image=self. photoimg5, borderwidth=0)
        # b1. place (x=960,y=160)

        # img6=Image.open("python/img3.jpeg")
        # img6=img6. resize((200,75))
        # self. photoimg6=ImageTk. PhotoImage (img6)
        # b1=Button(self.root, image=self. photoimg6, borderwidth=0)
        # b1. place (x=1160,y=160)
        
        lblrefno=Label(DataFramerRight,font=("arial",12,"bold"),text="Reference No:")
        lblrefno.place(x=0,y=10)
        txtrefno=Entry(DataFramerRight,textvariable=self.refMed_var,font=("arial",15,"bold"),bd=2,relief=RIDGE,width=14)
        txtrefno.place(x=135,y=10)

        lblmedName=Label(DataFramerRight,font=("arial",12,"bold"),text="Medicine Name:")
        lblmedName.place(x=0,y=50)
        txtmedName=Entry(DataFramerRight,textvariable=self.addmed_var,font=("arial",15,"bold"),bd=2,relief=RIDGE,width=14)
        txtmedName.place(x=135,y=50)


        #=========================side frame=========================

        side_frame=Frame(DataFramerRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=100,width=230,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        
        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")
        
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor)

        #====================Medicine Add Button====================
        down_frame=Frame(DataFramerRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=235,y=100,width=120,height=160)

        btnAddmed=Button(down_frame,text="Add", command=self.AddMed, font=("arial",12,"bold"),width=12,bg="lime",fg="black",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="UPDATE", command=self.Update_Med, font=("arial",12,"bold"),width=12,bg="purple",fg="black",pady=4)
        btnUpdatemed.grid(row=1,column=0)
        
        btnDeletemed=Button(down_frame,text="DELETE", command=self.deleteMed, font=("arial",12,"bold"),width=12,bg="red",fg="black",pady=4)
        btnDeletemed.grid(row=2,column=0)
        
        btnClearmed=Button(down_frame,text="CLEAR", command=self.clearMEd, font=("arial",12,"bold"),width=12,bg="orange",fg="black",pady=4)
        btnClearmed.grid(row=3,column=0)



        #======================Frame details=========================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1445,height=195 )


        #===================Main Table and Scrollbar==================
        Table_frame=Frame (Framedetails, bd=15, relief=RIDGE, padx=20)
        Table_frame. place (x=0,y=1,width=1500,height=180)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt")
                                         ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"
        
        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Expiry Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product QTs")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        
         
        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        #====================Add Medicine Functionality declaration====================

    def AddMed(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
        my_cursor=conn.cursor() 
        my_cursor.execute("INSERT INTO pharma(ref,med_name) VALUES(%s,%s)",(self.refMed_var.get(), self.addmed_var.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("success","Medicine Added")

    def fetch_dataMed(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
        my_cursor=conn.cursor() 
        my_cursor.execute("SELECT * FROM pharma")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("", END, values = i)

            conn.commit()
        conn.close()

    def Medget_cursor(self, event = ""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])

    def Update_Med(self):
        if self.refMed_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set med_name=%s WHERE ref = %s", (self.addmed_var.get(), self.refMed_var.get(),
            ))

            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success", "Data has been updated.")

    def deleteMed(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
        my_cursor=conn.cursor()
        sql = "Delete from pharma where ref=%s"
        val = (self.refMed_var.get(), )
        my_cursor.execute(sql, val)
        conn.commit()
        self.fetch_dataMed()
        conn.close()

    def clearMEd(self):
        self.refMed_var.set("")
        self.addmed_var.set("")


    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get() == "":
            messagebox.showerror("error","All fields are required")
        else :
            conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
            my_cursor=conn.cursor()    
            my_cursor.execute("INSERT INTO pharmacy VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.ref_var.get(),
            self.cmpname_var.get(),
            self.typeMed_var.get(),
            self.medName_var.get(),
            self.lot_var.get(),
            self.issuedate_var.get(),
            self.expdate_var.get(),
            self.uses_var.get(),
            self.sideeffect_var.get(),
            self.warning_var.get(),
            self.dosage_var.get(),
            self.price_var.get(),
            self.product_var.get()))    

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Data inserted.")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("", END, values = i)

            conn.commit()
        conn.close()

    def get_cursor(self,ev=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]


        self.ref_var.set(row[0]),
        self.cmpname_var.set(row[1]),
        self.typeMed_var_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_varot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideeffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12])

    def Update(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="PHW#84#jeor", database="PYTHON")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set c_name=%s,typemed=%s,medname=%s,lotno=%s,issuedate=%s,uses=%s,sideeffect=%s,warning=%s,dosage=%s,price=%s WHERE ref = %s", (self.ref_var.get(),
            self.cmpname_var.get(),
            self.typeMed_var.get(),
            self.medName_var.get(),
            self.lot_var.get(),
            self.issuedate_var.get(),
            self.expdate_var.get(),
            self.uses_var.get(),
            self.sideeffect_var.get(),
            self.warning_var.get(),
            self.dosage_var.get(),
            self.price_var.get(),
            self.product_var.get()
            ))

            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success", "Data has been updated.")


    


if __name__ == "__main__":
    main()