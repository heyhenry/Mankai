import ttkbootstrap as bttk
import tkinter as tk

class Windows(bttk.Window):
    def __init__(self, *args, **kwargs):
        bttk.Window.__init__(self, *args, **kwargs)

        self.style = bttk.Style(theme='darkly')

        self.title('Mankai')

        container = bttk.Frame(self, width=1100, height=700)
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
    
class RegisterPage(bttk.Frame):
    def __init__(self, parent, controller):
        bttk.Frame.__init__(self, parent)
        self.controller = controller

class LoginPage(bttk.Frame):
    def __init__(self, parent, controller):
        bttk.Frame.__init__(self, parent)
        self.controller = controller

class DiscoveryPage(bttk.Frame):
    def __init__(self, parent, controller):
        bttk.Frame.__init__(self, parent)
        self.controller = controller

class SearchPage(bttk.Frame):
    def __init__(self, parent, controller):
        bttk.Frame.__init__(self, parent)
        self.controller = controller

class MyListPage(bttk.Frame):
    def __init__(self, parent, controller):
        bttk.Frame.__init__(self, parent)
        self.controller = controller

class EntryPage(bttk.Frame):
    def __init__(self, parent, controller):
        bttk.Frame.__init__(self, parent)
        self.controller = controller

class SettingsPage(bttk.Frame):
    def __init__(self, parent, controller):
        bttk.Frame.__init__(self, parent)
        self.controller = controller




if __name__ == "__main__":
    app = Windows()
    app.mainloop()