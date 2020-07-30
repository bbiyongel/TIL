from  tkinter import *
root = Tk()
root.filename =  filedialog.askopenfilenames(initialdir = "E:/Images",title = "choose your file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

