# imports the tkinter module for the graphical user interface
import tkinter
from PIL import ImageTk,Image
import tkcap

def captureImage():
    cap = tkcap.CAP(root)
    cap.capture('joe.png')

    

# To center the window
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

# removes the main window when called
def change_window():

    
    window.destroy()

    root.iconify()
    root.deiconify()

    root.title('Quote Generator')
    root.geometry("500x500")
    center(root)

    image1 = Image.open("bird.png")
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=150, y=150)

    getImage = tkinter.Button(root, text="Save Image",padx=20,pady=20, command=captureImage)
    getImage.pack()
    getImage.place(x=200, y=50)
    

    root.resizable(width=0,height=0)




    


    

# creates a window instance
root = tkinter.Tk()
root.withdraw()


window = tkinter.Toplevel(root)


# a button that will run the getQuote function
getQuote = tkinter.Button(window, text="Generate Random Quote",padx=20,pady=20, command=change_window)
getQuote.pack()
getQuote.place(x=150, y=350)


# Sets title, window size and alignment
window.title('Quote Generator')
window.geometry("500x500")
window.resizable(width=0,height=0)
center(window)

# runs the thing
root.mainloop()