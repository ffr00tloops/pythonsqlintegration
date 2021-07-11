from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3


window = Tk()

connection = sqlite3.connect('test.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS `contacts` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, address TEXT, contactNum TEXT)")
connection.commit()


#center the main window
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

# Show Contacts



def showContacts():
    newWindow = Toplevel(window)
    newWindow.title("Contact Book")
    newWindow.geometry("700x300")
    newWindow.resizable(width=0,height=0)
    center(newWindow)
    rows = cursor.execute("""
        SELECT name,address,contactNum FROM contacts;
    """).fetchall

    Top = Frame(newWindow, width=700, height=60, bd=12, relief="raise")
    Top.pack(side=TOP)
    Button_Group=Frame(newWindow, width=700, height=50)
    Button_Group.pack(side=TOP)
    Buttons = Frame(Button_Group, width=200, height=50)
    Buttons.pack(side=LEFT)
    Buttons1 = Frame(Button_Group, width=500, height=50)
    Buttons1.pack(side=RIGHT)
    Body = Frame(newWindow, width=700, height=300, bd=8, relief="raise")
    Body.pack(side=BOTTOM)

    txt_title = Label(Top, width=300, font=('arial', 24), text = "Contacts")
    txt_title.pack()
 

    scrollbary = Scrollbar(Body, orient=VERTICAL)
    scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
    tree = ttk.Treeview(Body, columns=("Fullname", "Address", "ContactNum"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Fullname', text="Fullname", anchor=W)
    tree.heading('Address', text="Address", anchor=W)
    tree.heading('ContactNum', text="ContactNum", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.pack()

    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM contacts")
    fetch = cursor.fetchall()

    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2]))
    

    
def addContacts():
    newWindow = Toplevel(window)
    newWindow.title("Contact Book")
    newWindow.geometry("500x300")
    newWindow.resizable(width=0,height=0)
    center(newWindow)

    name_var = StringVar()
    address_var = StringVar()
    contact_var = StringVar()

    l1 = Label(newWindow, text="Full Name").place(x = 100, y = 20 )
    e1 = Entry(newWindow, textvariable=name_var, bd = 5 ).place(x = 100, y = 50)

    l2 = Label(newWindow, text="Address Name").place(x = 100, y = 100 )
    e2 = Entry(newWindow, textvariable=address_var, bd = 5 ).place(x = 100, y = 130)

    l3 = Label(newWindow, text="Contact Number").place(x = 100, y = 180 )
    e3 = Entry(newWindow, textvariable=contact_var, bd = 5 ).place(x = 100, y = 210)



    def insertData():        
        name = name_var.get()
        address = address_var.get()
        contact = contact_var.get()

        print(name)
        print(address)
        print(contact)

        cursor.execute(f"INSERT INTO contacts(name,address,contactNum) VALUES ('{name}','{address}','{contact}')")
        newWindow.destroy()

    button = Button(newWindow,command=insertData, text="Insert Data").place( x = 300, y = 130)







    





# View
def view():
    label1 = Label(window, font=("Arial", 25), text="Contact Book").place( x=150, y = 60)
    showBtn = Button(window, command=showContacts ,text="Show all contacts").place(x = 195, y = 200)
    addBtn = Button(window, command=addContacts , text="Add New Contact" ).place(x = 195, y = 250)
    modifyBtn = Button(window, text="Modify Existing Contact").place( x = 180,y = 300)
    deleteBtn = Button(window, text="Delete  Existing Contact").place(x = 180, y = 350)



#set window size
window.title("Contact Book")
window.geometry("500x500")
window.resizable(width=0,height=0)
center(window)


view()


window.mainloop()

