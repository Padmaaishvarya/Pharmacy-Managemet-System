import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Create a database connection and cursor
conn = sqlite3.connect('pharmacy.db')
cursor = conn.cursor()

# Create the pharmacy table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS pharmacy (
    S_No INTEGER PRIMARY KEY AUTOINCREMENT,
    Name_of_Tablets TEXT,
    Reference_No TEXT,
    Dose TEXT,
    No_of_Tablets INTEGER,
    Manufacturing_date DATE,
    Expiry_Date DATE
)
''')
conn.commit()

def add_entry():
    name = name_entry.get()
    ref = ref_entry.get()
    dose = dose_entry.get()
    no_of_tablets = int(no_of_tablets_entry.get())
    issue_date = issue_date_entry.get()
    exp_date = exp_date_entry.get()

    # Insert the data into the database
    cursor.execute('INSERT INTO pharmacy (Name_of_Tablets, Reference_No, Dose, No_of_Tablets, Manufacturing_date, Expiry_Date) VALUES (?, ?, ?, ?, ?, ?)',
                   (name, ref, dose, no_of_tablets, issue_date, exp_date))
    conn.commit()

    messagebox.showinfo("Success", "Entry added successfully")

def show_entries():
    result_window = tk.Toplevel(root)
    result_window.title("Pharmacy Entries")
    result_window.geometry("600x400")

    result_tree = ttk.Treeview(result_window, columns=("S.No.","Name", "Reference No", "Dose", "No. of Tablets", "Issue Date", "Exp Date"))
    result_tree.heading("#1", text="S.No.")
    result_tree.heading("#2", text="Name of Tablets")
    result_tree.heading("#3", text="Reference No")
    result_tree.heading("#4", text="Dose")
    result_tree.heading("#5", text="No. of Tablets")
    result_tree.heading("#6", text="Issue Date")
    result_tree.heading("#7", text="Exp Date")
    result_tree.pack()

    # Fetch and display data from the database
    cursor.execute("SELECT * FROM pharmacy")
    rows = cursor.fetchall()
    for i, row in enumerate(rows, start=1):
        result_tree.insert("", "end", values=(i, *row[1:]))

# Create the main application window
root = tk.Tk()
root.title("Pharmacy Management System")

# Create entry fields and labels
name_label = tk.Label(root, text="Name of Tablets:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

ref_label = tk.Label(root, text="Reference No:")
ref_label.pack()
ref_entry = tk.Entry(root)
ref_entry.pack()

dose_label = tk.Label(root, text="Dose:")
dose_label.pack()
dose_entry = tk.Entry(root)
dose_entry.pack()

no_of_tablets_label = tk.Label(root, text="No. of Tablets:")
no_of_tablets_label.pack()
no_of_tablets_entry = tk.Entry(root)
no_of_tablets_entry.pack()

issue_date_label = tk.Label(root, text="Issue Date:")
issue_date_label.pack()
issue_date_entry = tk.Entry(root)
issue_date_entry.pack()

exp_date_label = tk.Label(root, text="Exp Date:")
exp_date_label.pack()
exp_date_entry = tk.Entry(root)
exp_date_entry.pack()

add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.pack()

show_button = tk.Button(root, text="Show Entries", command=show_entries)
show_button.pack()

root.geometry("400x400")
root.mainloop()

# Close the database connection when the application exits
conn.close()
