from tkinter import *
from PIL import Image, ImageTk
#creating blank GUI page
root= Tk()

#setting the page size
root.geometry("733x434")

#root.minsize(333,234)
#root.maxsize(933,634)


img=Image.open("C:\\Users\\USER\Desktop\Shubham\Image folder\Image1.jpg")

photo=ImageTk.PhotoImage(img)

labl=Label(image=photo, justify='center')
labl.pack()

root.mainloop()