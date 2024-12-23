from tkinter import *
from tk_mainpage import MainPage
from tk_peoplepage import PeoplePage
from tk_eventspage import EventsPage
from buttons_operations.add_people import Add_People

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("P&E Track")
        self.geometry("500x600")
        self.resizable(False, False)
        self.config(background='#333333')

        # Container pentru pagini
        self.container = Frame(self, bg="#333333")
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        # Adăugăm paginile
        for Page in (MainPage, PeoplePage, EventsPage, Add_People):
            page_name = Page.__name__
            frame = Page(parent=self.container, controller=self)
            self.frames[page_name] = frame

        self.show_frame("MainPage")  # Afișăm MainPage la început

    def show_frame(self, page_name):
        """Afișează cadrul selectat și ascunde celelalte."""
        for frame in self.frames.values():
            frame.pack_forget()  # Ascundem toate cadrele
        self.frames[page_name].pack(fill="both", expand=True)  # Afișăm cadrul selectat

if __name__ == "__main__":
    app = App()
    app.mainloop()
