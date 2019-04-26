from tkinter import Tk,scrolledtext,Menu,filedialog,END,messagebox,simpledialog
import os
root=Tk(className="Notepad")
textArea=scrolledtext.ScrolledText(root,width=100,height=100)



def newFile():
    if (len(textArea.get('1.0',END+ '-1c'))>0):
        if messagebox.askyesno("save","Do you want to save?"):
            saveFile()
            textArea.delete('1.0',END)
        else:
            textArea.delete('1.0',END)
    root.title('TEXT EDITOR')
def openFile():
    textArea.delete('1.0',END)
        
    file=filedialog.askopenfile(parent=root,title="Select a File below",filetypes=(("text file","*.txt"),("All files","*.*")))
    root.title(os.path.basename(file.name)+ '-TEXT EDITOR')
               
    if file!=None:
        contents=file.read()
        textArea.insert('1.0',contents)
        file.close()

def saveFile():
    file=filedialog.asksaveasfile(mode="w")
    if file!=None:
        data = textArea.get('1.0',END+ '-1c')
        file.write(data)
        file.close()
def Exit():
    if messagebox.showinfo("Quit","Are you sure you want to quit?"):
        root.destroy()
def about():
    label=messagebox.showinfo("About","A Notepad using Python")
def Find():
    find=simpledialog.askstring("Find..","Enter Text")
    textData=textArea.get('1.0',END)
    c=textData.upper().count(find.upper())
    if textData.upper().count(find.upper())>0:
        label=messagebox.showinfo("Results", find+ " has "+str(c)+"occurances")
    else:
        label=messagebox.showinfo("Sorry! word not found")
    
               
    
    
menu=Menu(root)
root.config(menu=menu)
fileMenu=Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=newFile)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_command(label="Find",command=Find)

fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=Exit)

helpMenu=Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About",command=about)



textArea.pack()

root.mainloop()
