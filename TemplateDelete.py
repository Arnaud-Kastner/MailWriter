#################################
### Created by Arnaud KASTNER ###
#################################

import tkinter as tk
from lib import Redactor

class DeleteTemplate :
    def __init__ (self) :
        self.lib = Redactor()
        self.nb_file = self.lib.nb_finder()  
    
    def start(self) :
        self.root = tk.Tk()
        self.root.title("Mail Redactor")
        
        self.title = tk.Label(self.root, text="Template Deletion Menu",font=("Arial",20))
        self.title.grid(row=0,column=0)
        
        self.template_list = tk.Listbox(self.root)
        self.template_list.grid(row=1,column=0)
        
        self.refresh_btn = tk.Button(self.root, text="Refresh the list", command=self.refresh_list)
        self.refresh_btn.grid(row=2,column=0)
        self.refresh_list()
        
        self.root.mainloop()
        
    def refresh_list(self) :
        
        self.template_list.delete(0,tk.END)
        name_liste = self.lib.list_finder()
        self.template_list.insert(tk.END,str(self.lib.list_finder))
  
        # for file_found in range (1,tot_file) :
        #     
        #     if self.lib.ver_file_exist(file_name) == True :

        #         file_found+=1
        #         print("True")
        #     else :
        #         print("False")
        #         tot_file+=1
        
        # print(tot_file)
        # print(self.file_list)
