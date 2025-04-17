import customtkinter as ctk
import tkinter as tk

class Windows(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        self.title('Mankai')

        container = ctk.CTkFrame(self, width=1100, height=700)
        container.grid_propagate(False)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}

        for P in (RegisterPage, LoginPage, DiscoveryPage, SearchPage, MyListPage, EntryPage, SettingsPage):
            page = P(container, self)
            self.pages[P] = page
            page.grid(row=0, column=0, sticky='nswe')

        self.show_page(RegisterPage)

    def show_page(self, current_page):
        page = self.pages[current_page]
        page.tkraise()
    
class RegisterPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        show_register = ctk.CTkLabel(self, text='Register Page!')
        switch = ctk.CTkButton(self, text='Switch to Login.', command=lambda: self.controller.show_page(LoginPage))

        show_register.pack()
        switch.pack()

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        show_register = ctk.CTkLabel(self, text='Login Page!')
        switch = ctk.CTkButton(self, text='Switch to Register.', command=lambda: self.controller.show_page(RegisterPage))

        show_register.pack()
        switch.pack()

class DiscoveryPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

class SearchPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

class MyListPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

class EntryPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

class SettingsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller




if __name__ == "__main__":
    app = Windows()
    app.mainloop()