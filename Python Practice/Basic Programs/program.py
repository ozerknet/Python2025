import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Veritabanı oluşturma veya bağlanma
def create_table():
    conn = sqlite3.connect('Contacts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Yeni kişi ekleme formu
def open_registration_form():
    form_window = tk.Toplevel(root)
    form_window.title("New Contact")
    form_window.geometry("300x250")

    tk.Label(form_window, text="First Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_first_name = tk.Entry(form_window)
    entry_first_name.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form_window, text="Last Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_last_name = tk.Entry(form_window)
    entry_last_name.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(form_window, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_phone = tk.Entry(form_window)
    entry_phone.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(form_window, text="Email Address:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_email = tk.Entry(form_window)
    entry_email.grid(row=3, column=1, padx=10, pady=5)

    def submit_form():
        first_name = entry_first_name.get().strip()
        last_name = entry_last_name.get().strip()
        phone = entry_phone.get().strip()
        email = entry_email.get().strip()

        if not all([first_name, last_name, phone, email]):
            messagebox.showwarning("Missing Information", "Please fill out all fields.")
            return

        try:
            conn = sqlite3.connect('Contacts.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Contacts (first_name, last_name, phone, email)
                VALUES (?, ?, ?, ?)
            ''', (first_name, last_name, phone, email))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Contact saved successfully.")
            form_window.destroy()
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    tk.Button(form_window, text="Save", command=submit_form).grid(row=4, column=0, columnspan=2, pady=10)

# Kişi güncelleme formu
def open_update_form(contact):
    update_window = tk.Toplevel(root)
    update_window.title("Update Contact")
    update_window.geometry("300x250")

    tk.Label(update_window, text="First Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_first_name = tk.Entry(update_window)
    entry_first_name.grid(row=0, column=1, padx=10, pady=5)
    entry_first_name.insert(0, contact[1])

    tk.Label(update_window, text="Last Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_last_name = tk.Entry(update_window)
    entry_last_name.grid(row=1, column=1, padx=10, pady=5)
    entry_last_name.insert(0, contact[2])

    tk.Label(update_window, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_phone = tk.Entry(update_window)
    entry_phone.grid(row=2, column=1, padx=10, pady=5)
    entry_phone.insert(0, contact[3])

    tk.Label(update_window, text="Email Address:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_email = tk.Entry(update_window)
    entry_email.grid(row=3, column=1, padx=10, pady=5)
    entry_email.insert(0, contact[4])

    def update_contact():
        first_name = entry_first_name.get().strip()
        last_name = entry_last_name.get().strip()
        phone = entry_phone.get().strip()
        email = entry_email.get().strip()

        if not all([first_name, last_name, phone, email]):
            messagebox.showwarning("Missing Information", "Please fill out all fields.")
            return

        try:
            conn = sqlite3.connect('Contacts.db')
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Contacts
                SET first_name = ?, last_name = ?, phone = ?, email = ?
                WHERE id = ?
            ''', (first_name, last_name, phone, email, contact[0]))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Contact updated successfully.")
            update_window.destroy()
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    tk.Button(update_window, text="Update", command=update_contact).grid(row=4, column=0, columnspan=2, pady=10)

# Kişileri listeleme ve silme
def list_contacts():
    list_window = tk.Toplevel(root)
    list_window.title("Contact List")
    list_window.geometry("600x400")

    tree = ttk.Treeview(list_window, columns=('ID', 'First Name', 'Last Name', 'Phone', 'Email'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('First Name', text='First Name')
    tree.heading('Last Name', text='Last Name')
    tree.heading('Phone', text='Phone')
    tree.heading('Email', text='Email')
    tree.pack(fill='both', expand=True)

    def load_contacts():
        for row in tree.get_children():
            tree.delete(row)
        try:
            conn = sqlite3.connect('Contacts.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Contacts')
            rows = cursor.fetchall()
            for row in rows:
                tree.insert('', tk.END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def on_double_click(event):
        selected_item = tree.selection()
        if not selected_item:
            return
        item = tree.item(selected_item)
        contact = item['values']
        open_update_form(contact)

    def delete_selected():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a contact to delete.")
            return
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected contact?")
        if confirm:
            try:
                item = tree.item(selected_item)
                contact_id = item['values'][0]
                conn = sqlite3.connect('Contacts.db')
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Contacts WHERE id = ?', (contact_id,))
                conn.commit()
                conn.close()
                tree.delete(selected_item)
                messagebox.showinfo("Success", "Contact deleted successfully.")
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")

    tree.bind("<Double-1>", on_double_click)

    tk.Button(list_window, text="Delete Selected", command=delete_selected).pack(pady=10)

    load_contacts()

# Ana pencereyi oluşturma
root = tk.Tk()
root.title("Contact Management")
root.geometry("300x250")

# Veritabanı tablosunu oluşturma
create_table()

# Butonları oluşturma
tk.Button(root, text="New Contact", width=20, command=open_registration_form).pack(pady=10)
tk.Button(root, text="List Contacts", width=20, command=list_contacts).pack(pady=10)
tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=10)

# Ana döngüyü başlatma
root.mainloop()
