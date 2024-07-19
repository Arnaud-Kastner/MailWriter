import tkinter as tk

class MyGUI:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Mail Redactor")

        self.titre = tk.Label (self.root, text="Ecrire un mail", font=('Arial', 20))
        self.titre.pack(padx=20,pady=20)

        self.text_ent = tk.Label (self.root, text="Rédiges ton mail : ")
        self.text_ent.pack(padx=20,pady=20)

        self.En_ent = tk.Entry(self.root)
        self.En_ent.pack(padx=20,pady=20)


        self.test_button = tk.Button(self.root, text="Test print", command=self.affichage)
        self.test_button.pack(padx=10,pady=20)
        
        self.root.mainloop()

    def affichage (self) :
        print("Test Clear")

MyGUI()

