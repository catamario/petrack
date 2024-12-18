from tkinter import *

window = Tk()
window.geometry('500x600')
window.title('P&E Track')

window.config(background='#333333')

header = Frame(window, bg="#282828", height=75)
header.pack(fill="x")

header_label = Label(header, text="People & Events Tracker", bg='#282828', fg='#66BB6A', font=("Arial", 20, "bold"))
header_label.pack(pady=20)

welcome_frame = Frame(window, bg="#333333")  # Frame transparent (aceeași culoare ca fundalul)
welcome_frame.pack(pady=20)

# Primul Label pentru cuvântul "Welcome", cu stil bold
welcome_label = Label(
    welcome_frame,
    text="Welcome!",
    bg="#333333",  # Fundal transparent (același ca fereastra principală)
    fg="#BDFDC0",  # Text alb
    font=("Arial", 16, "bold"),  # Font bold pentru "Welcome"
    justify="center"
)
welcome_label.pack()

# Al doilea Label pentru restul textului
rest_of_text_label = Label(
    welcome_frame,
    text="The best solution for managing people and events effortlessly.",
    bg="#333333",  # Fundal transparent
    fg="#BDFDC0",  # Text alb
    font=("Arial", 14),
    justify="center",
    wraplength=450
)
rest_of_text_label.pack()
#icon = PhotoImage(file='logo.png')
#window.iconphoto(True, icon)

buttons_div = Frame(window, bg="#333333", height=300)
buttons_div.pack(pady=10, fill="x")

buttons_frame = Frame(buttons_div, bg="#FFFFFF")  # Frame nou pentru butoane
buttons_frame.grid(sticky="ew")

# Buton People
people_button = Button(
    buttons_frame,
    text="People",
    bg="#66BB6A",  # Verde deschis
    fg="white",
    font=("Arial", 12, "bold"),
    width=10,
    relief="flat"
)
people_button.grid(row=0, column=0, padx=10)  # Grid pentru poziționare

# Buton Events
events_button = Button(
    buttons_frame,
    text="Events",
    bg="#66BB6A",
    fg="white",
    font=("Arial", 12, "bold"),
    width=10,
    relief="flat"
)
events_button.grid(row=0, column=1, padx=10)


window.mainloop()