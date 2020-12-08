from tkinter import messagebox
from tkinter import *
import webbrowser
import pyperclip
import random
import os


root = Tk()
root.title('Contact Book')
root.geometry('650x300')
background = '#121212'
root.config(bg=background)

# ✔
# Contact Name Label  ✔
# Contact Name Entry ✔

# Contact Number Label ✔
# Contact Number Entry ✔

# Add contact Button ✔
# Save List Button ✔

# Copy Phone Number Button ✔
# Open Saved File Button ✔
# Delete Contact Button ✔
# Exit App Button ✔

# ListBox For Contacts ✔


# Functions
def add_contact():
    contact_string = name_entry.get() + ': ' + phone_entry.get()
    listbox.insert(END, contact_string)
    
    name_entry.delete(0,END)
    phone_entry.delete(0,END)

def delete_contact():
    listbox.delete(ANCHOR)

def save_list():
    """ Save the list to a simple txt file """
    
    with open('D:\Python Programming\Aparat Stream\Contact Book\saved.txt', 'w') as f:
        list_tuple = listbox.get(0,END)
        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item+'\n')


def open_list():
    with open('D:\Python Programming\Aparat Stream\Contact Book\saved.txt', 'r') as f:
        for line in f:
            listbox.insert(END, line)

def open_dir():
    webbrowser.open('D:\Python Programming\Aparat Stream\Contact Book')

def copy_number():
    selected_contact = listbox.get(ANCHOR)
    number = selected_contact.split(': ')
    pyperclip.copy(number[1].replace('\n',""))

def exit():
    choice = messagebox.askquestion('Exit Aplication', 'Are you sure you want to close the application?')
    if choice == 'yes':
        root.destroy()
    else:
        return

# Contact Name Label And Entry
name_label = Label(root, text='Contact Name:', bg=background, fg='white', font=('Calibri', 12), anchor='w', justify=LEFT)
name_label.place(relx=0.1, rely=0.1, anchor='c')

name_entry = Entry(root, bg='white', fg=background, width=30, borderwidth=2)
name_entry.place(relx=0.4, rely=0.1, anchor='c')

# Contact Number Label And Entry
phone_label = Label(root, text='   Contact Number:', bg=background, fg='white', font=('Calibri', 12), anchor='w', justify=LEFT)
phone_label.place(relx=0.1, rely=0.2, anchor='c')

phone_entry = Entry(root, bg='white', fg=background, width=30, borderwidth=2)
phone_entry.place(relx=0.4, rely=0.2, anchor='c')

# Add Contact Button
add_btn = Button(root, text='Add Contact', bg='#121212', fg='white', borderwidth=3, padx=125, command=add_contact  )
add_btn.place(relx=0.29, rely=0.35, anchor='c')

# Save List Button
save_btn = Button(root, text='Save List', bg=background, fg='white', borderwidth=3, padx=135, command=save_list)
save_btn.place(relx=0.29, rely=0.5, anchor='c')

# Copy Phone Number Button
copyPhone = Button(root, text='Copy Phone Number', bg=background, fg='white', borderwidth=3, padx=10, command=copy_number)
copyPhone.place(relx=0.15, rely=0.65, anchor='c')

# Delete Contact Button
deletePhone = Button(root, text='Delete Contact ', bg=background, fg='white', borderwidth=3, padx=25, command=delete_contact)
deletePhone.place(relx=0.15, rely=0.77, anchor='c')

# Open Saved File Button
openSaved = Button(root, text='Open Saved File ', bg=background, fg='white', borderwidth=3, padx=30, command=open_dir)
openSaved.place(relx=0.42, rely=0.65, anchor='c')

# Exit App Button
exit = Button(root, text='Exit App', bg=background, fg='white', borderwidth=3, padx=50, command=exit)
exit.place(relx=0.42, rely=0.77, anchor='c')

# List Box For Contacts
listbox = Listbox(root, width=40, height=15)
listbox.place(relx=0.75, rely=0.47, anchor='c')

open_list()
root.mainloop()