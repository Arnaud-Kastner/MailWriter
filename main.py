#################################
### Created by Arnaud KASTNER ###
#################################

import tkinter as tk
from TemplateAdd import AddTemplate
from TemplateDelete import DeleteTemplate

class Main_Menu:
    def __init__(self) :
        self.menu= tk.Tk()
        self.menu.title("Mail Redactor")
        
        self.titre = tk.Label (self.menu, text="Welcome to Mail Redactor",font=("Arial",20))
        self.titre.grid()
        
        self.frame_btn = tk.Frame(self.menu)
        self.frame_btn.grid(row=1,column=0)
        
        self.wr_btn = tk.Button (self.frame_btn,text="Write your mail", command=self.writer)
        self.wr_btn.grid(row=0,column=0)
        
        self.add_btn = tk.Button (self.frame_btn, text="Add a template",command=self.add_template)
        self.add_btn.grid(row=0,column=1)
        
        self.del_btn = tk.Button(self.frame_btn,text = "Delete a template", command=self.del_template)
        self.del_btn.grid(row=0,column=2)
        
        self.close_btn = tk.Button(self.frame_btn,text="Close the app",command=self.menu.destroy)
        self.close_btn.grid(row=0,column=3)
        
        self.menu.mainloop()
    
    def writer(self) :
        print("writer")
    
    def add_template(self) :
        add_menu = AddTemplate()
        add_menu.start()
    
    def del_template(self) :
        del_menu = DeleteTemplate()
        del_menu.start()

Main_Menu()
