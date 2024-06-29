import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector as sql

def connect_to_db():
    return sql.connect(user="root", host="localhost", password="mysql@2005", database="Janvi")

def add_record():
    def submit_record():
        name = entry_name.get()
        age = entry_age.get()
        gender = entry_gender.get()
        weight = entry_weight.get()
        height = entry_height.get()
        ft_goals = entry_ft_goals.get()
        ht_cond = entry_ht_cond.get()
        
        try:
            db = connect_to_db()
            cursor = db.cursor()
            query = "INSERT INTO userdata (name, age, gender, weight, height, ft_goals, ht_cond) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (name, age, gender, weight, height, ft_goals, ht_cond))
            db.commit()
            db.close()
            messagebox.showinfo("Success", "Record entered successfully")
        except sql.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    record_window = tk.Toplevel(root)
    record_window.title("Add Record")

    tk.Label(record_window, text="Name").grid(row=0, column=0)
    tk.Label(record_window, text="Age").grid(row=1, column=0)
    tk.Label(record_window, text="Gender").grid(row=2, column=0)
    tk.Label(record_window, text="Weight").grid(row=3, column=0)
    tk.Label(record_window, text="Height").grid(row=4, column=0)
    tk.Label(record_window, text="Fitness Goals").grid(row=5, column=0)
    tk.Label(record_window, text="Health Conditions").grid(row=6, column=0)

    entry_name = tk.Entry(record_window)
    entry_age = tk.Entry(record_window)
    entry_gender = tk.Entry(record_window)
    entry_weight = tk.Entry(record_window)
    entry_height = tk.Entry(record_window)
    entry_ft_goals = tk.Entry(record_window)
    entry_ht_cond = tk.Entry(record_window)

    entry_name.grid(row=0, column=1)
    entry_age.grid(row=1, column=1)
    entry_gender.grid(row=2, column=1)
    entry_weight.grid(row=3, column=1)
    entry_height.grid(row=4, column=1)
    entry_ft_goals.grid(row=5, column=1)
    entry_ht_cond.grid(row=6, column=1)

    submit_btn = tk.Button(record_window, text="Submit", command=submit_record)
    submit_btn.grid(row=7, column=1)

def user_options():
    user_window = tk.Toplevel(root)
    user_window.title("User Options")

    def on_option_select():
        ch2 = int(user_choice.get())
        if ch2 == 1:
            add_record()
        elif ch2==2:
            print("1.. 30 day workout plan ")
            print("2.. 7 day workout plan")
            ch4=int(input("Enter your choice: "))
            if ch4==1:
                db = connect_to_db()
                cursor = db.cursor()
                query = "select * from 30daysworkout"
                cursor.execute(query)
                result=cursor.fetchall()
                db.commit()
                db.close()
                for i in result:
                    print(i)
            else:
                db1= connect_to_db()
                cursor1 = db1.cursor()
                query1 = "select * from 7daysintermediateworkout"
                cursor1.execute(query1)
                result1=cursor1.fetchall()
                db1.commit()
                db1.close()
                for i in result1:
                    print(i)
                #print(result1)
        # Further options can be added here following the same pattern.

    tk.Label(user_window, text="1...User Profile").pack()
    tk.Label(user_window, text="2...Personalized Workout Plans").pack()
    tk.Label(user_window, text="3...Nutrition and Diet Plans").pack()
    tk.Label(user_window, text="4...Activity Tracking").pack()
    tk.Label(user_window, text="5...Exit").pack()

    user_choice = tk.Entry(user_window)
    user_choice.pack()

    select_btn = tk.Button(user_window, text="Select", command=on_option_select)
    select_btn.pack()

def main():
    root.title("Main Menu")
    tk.Label(root, text="-------------Enter your choice-------------").pack()
    tk.Label(root, text="1...USER").pack()
    tk.Label(root, text="2...TRAINERS").pack()
    tk.Label(root, text="3...ADMINISTRATORS").pack()

    main_choice = tk.Entry(root)
    main_choice.pack()

    def on_main_choice():
        ch1 = int(main_choice.get())
        if ch1 == 1:
            user_options()
        # Further main options can be added here following the same pattern.

    select_btn = tk.Button(root, text="Select", command=on_main_choice)
    select_btn.pack()

root = tk.Tk()
main()
root.mainloop()
