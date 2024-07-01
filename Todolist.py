from tkinter import *
from tkinter import ttk

class todolist:
    def __init__(self, root): 
        self.root = root
        self.root.title('To Do List')
        self.root.geometry('750x700+0+0')

        self.label = Label(self.root, text='To-do-List', 
                           font='serif, 30 bold', width=10, bd=5, bg='red',fg='black')
        self.label.pack (side='top', fill=BOTH)
        
        self.label = Label(self.root, text='Input Tasks', 
                           font='serif, 15 bold', width=10, bd=5, bg='yellow',fg='black')
        self.label.place (x=120, y=59)
        
        self.label = Label(self.root, text='Tasks', 
                           font='serif, 15 bold', width=10, bd=5, bg='yellow',fg='black')
        self.label.place (x=480, y=59)
        
        self.main_text = Listbox(self.root, height = 20, width=30, font="serif" )
        self.main_text.place (x=380, y=110)
        
        self.text= Text(self.root, bd=5, height=2, width=30, font='serif, 15 bold')
        self.text.place(x=20, y=120)
       
       #------------------- Input Task --------------------#
         
        def input():
            content = self.text.get(1.0,END)
            self.main_text.insert(END, content)
            with open('data.txt','w') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)
        def delete():
            delete_=self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt','r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                    f.truncate()
                self.main_text.delete(delete_)
                
            with open('data.txt','r') as file:
                read = file.readlines()
                for i in read:
                    ready = i.split()
                    self.main_text.insert(END,ready)
                file.close()
        
        self.button = Button(self.root, text="Input", font='sarif 15 bold', width=10, bd=5, bg='red', fg='black', command=input)
        self.button.place(x=120, y=210)
                
        self.button2 = Button(self.root, text="Delete", font='sarif 15 bold', width=10, bd=5, bg='red', fg='black', command=delete)
        self.button2.place(x=120, y=290)
        
def main():
    root = Tk()
    ui = todolist(root)
    root.mainloop()

if __name__ == "__main__":
    main()