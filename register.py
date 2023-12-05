from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # pip install pillow
from tkinter import messagebox
import mysql.connector

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
        loginbtn = Button(frame, text="Login", font=("Times New Roman", 16, "bold"), bd=3, relief=RIDGE, fg="white", bg="black", activebackground="black", activeforeground="white")
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

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
        