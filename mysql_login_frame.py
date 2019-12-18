#just some updates are added in this file
import tkinter as tk
import mysql.connector as mc
from tkinter import messagebox as mb
import re
import sys

window = tk.Tk()
window.geometry('400x300')
window.title('Testing from the Git command line')
window.resizable(False, False)
connect = mc.connect(host='localhost', db='rajat', user='rajat', password='9711289764')
if connect.is_connected():
    print('you are in...')


class Sign_up:
    def __init__(self, self.top_frame):
        self.top_frame = tk.Frame(self.top_frame)
        self.user_name = tk.Label(self.top_frame, text='User Name')
        self.user_name_entry = tk.Entry(self.top_frame)
        self.password = tk.Label(self.top_frame, text="Passsword")
        self.password_entry = tk.Entry(self.top_frame)
        self.confirm_password = tk.Label(self.top_frame, text='''Confirm 
Password''')
        self.confirm_password_entry = tk.Entry(self.top_frame)
        self.check_button = tk.Button(self.top_frame, text='Create Account', command=self.check)
        self.exit_button = tk.Button(self.top_frame, text='Cancel', command=self.Exit)
        self.exit_button.grid(row=9, column=3)
        self.auto_label = tk.Label(self.top_frame, text='User name cannot be empty',fg='red')
        self.mailid = tk.Label(self.top_frame, text='Email ID')
        self.mailid.entry = tk.Entry(self.top_frame)
        self.user_name.grid(row=0, column=2)
        self.user_name_entry.grid(row=0, column=5)
        self.password.grid(row=3, column=2)
        self.password_entry.grid(row=3, column=5)
        self.confirm_password.grid(row=5, column=2)
        self.confirm_password_entry.grid(row=5, column=5)
        self.mailid.grid(row=7, column=2)
        self.mailid.entry.grid(row=7, column=5)
        self.check_button.grid(row=9, column=5)
        self.auto_label.grid(row=10,column=5)

    def Exit(self):
        sys.exit()

    def mailid(self):
        mail =self.mailid.entry.get()
        if re.search('@', mail) is None:
            self.auto_label.configure(text='please provide a valid email id')

    def check(self):
        flag = 0
        cursor = connect.cursor()
        cursor.execute('select * from db')
        rows = cursor.fetchall()

        entry = self.user_name_entry.get()
        print(len(entry))
        for row in rows:
            if len(entry) == 0:

                flag = 2
                break
            elif entry == row[0]:
                flag = 1
                break
            else:
                flag = 0

        if flag == 2:
            self.auto_label.configure(text='User name cannot be empty')
        elif flag == 1:
            mb.showinfo("Error", 'User Exists!')
        else:
            self.password_checker()
            if self.pass_flag == 0:
                self.confirm_pass()
                if self.confirm_pass_flag == 1:
                    password = self.password_entry.get()
                    query = """insert into db (name,password) values(%s, %s)"""
                    values = (entry, password)
                    try:
                        cursor.execute(query, values)
                        connect.commit()
                        self.user_name_entry.delete(first=0, last=30)
                        self.password_entry.delete(first=0, last=30)
                        self.confirm_password_entry.delete(first=0, last=30)
                        print('Record Insert successfully!')
                    except:
                        connect.rollback()
                        print("Connection has been roll back")
                else:
                    mb.showinfo("Error", "Confirm Password Doesn't matched with Password")

    def confirm_pass(self):

        if self.pass_flag == 0:
            self.confirm_pass_flag = 0
            confirm_pass = self.confirm_password_entry.get()
            password = self.password_entry.get()
            if password == confirm_pass:
                self.confirm_pass_flag = 1
            else:
                self.confirm_pass_flag = 0

    # def user_input(self):
    #     while True:
    #         if len(self.user_name_entry.get()) == 0:
    #             self.auto_label.configure(text='User name cannot be empty')

    def password_checker(self):
        password = self.password_entry.get()
        self.pass_flag = 0
        while True:
            if len(password) < 8:
                mb.showinfo('Error', 'Password Length should be atleast 8 character long:')
                self.pass_flag = 1
                break
            elif re.search('[A-Z]', password) is None:
                mb.showinfo('Error', 'Password should have atleast one Capital Letter:')
                self.pass_flag = 1
                break
            elif re.search('[0-9]', password) is None:
                mb.showinfo('Error', 'Password should have atleast one Number')
                self.pass_flag = 1
                break
            elif re.search('[!@#$%^&*]', password) is None:
                mb.showinfo('Error', 'Password should have atleast one special character!')
                self.pass_flag = 1
                break
            else:
                print('password is in order')
                self.pass_flag = 0
                break


obj = Sign_up(window)
# this is te changes that i applied in this file using VIM Editor

window.mainloop()
