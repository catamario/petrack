from tkinter import *

class Add_People(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")
        self.controller = controller

        # Header
        header = Frame(self, bg="#282828", height=75)
        header.pack(fill="x")
        header_label = Label(
            header, text="People & Events Tracker", bg='#282828', fg='#66BB6A', font=("Arial", 20, "bold")
        )
        header_label.pack(pady=20)

        # Content
        content_label = Label(
            self, text="ADD PEOPLE", bg="#333333", fg="#BDFDC0", font=("Arial", 20, "bold"), justify="center"
        )
        content_label.pack(pady=30)


        div_Form = Frame(self, bg="#333333", height=250)
        div_Form.pack(pady=5, fill="x")
        form = Frame(div_Form, bg="#333333", height=250)
        form.place(anchor = "e", relx="0.9", rely="0.5")

        # ID
        id_label = Label(form, text="id:", font=("Arial", 20), fg="#FFFFFF", bg="#333333")
        id_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        id_entry = Entry(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000")
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Nume
        name_label = Label(form, text="name:", font=("Arial", 20), fg="#FFFFFF", bg="#333333")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        name_entry = Entry(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000")
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        # Adress
        address_label = Label(form, text="adress:", font=("Arial", 20), fg="#FFFFFF", bg="#333333")
        address_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        address_entry = Entry(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000")
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        # Mesaj de confirmare
        confirmation_label = Label(form, text="MESAJ DE CONFIRMARE\nROSU/VERDE", font=("Arial", 14, "bold"), fg="#FF0000", bg="#333333")
        confirmation_label.grid(row=3, column=1, padx=10, pady=5)

        # ADD BUTTON
        add_button = Button(
            self,
            text="ADD",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 14, "bold"),
            width=15, height=2,
            relief="flat",
        )
        add_button.pack()

        # Back Button
        back_button = Button(
            self,
            text="Back to Main",
            bg="#9DBA4D",
            fg="white",
            font=("Arial", 14, "bold"),
            width=15,height=2,
            relief="flat",
            command=lambda: controller.show_frame("PeoplePage")  # Navighează înapoi la MainPage
        )
        back_button.pack(pady=10)