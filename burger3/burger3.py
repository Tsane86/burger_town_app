# Documentation
"""Ordering GUI App for Codetown Burger Co
    Prgram will display a interface for the user to use to see the details of each burger.
    By default, the first option of Byte Burger is displayed.
    User can click on each button to see the details of the burger.

    Type python3 burger3.py to run the program. This will launch the GUI interface.
"""

# import packages
import tkinter as tk

# set up class for burger
class Burger:
    def __init__(self, name, type_of_bun, sauce, patties, cheese, tomato, lettuce, onion, cost):
        self.name = name
        self.bun = type_of_bun
        self.sauce = sauce
        self.patties = patties
        self.cheese = cheese
        self.tomato = tomato
        self.lettuce = lettuce
        self.onion = onion
        self.cost = cost
    
    def __str__(self):
        return f'Name: {self.name}, Type of Bun: {self.bun}, Sauce: {self.sauce}, Patties: {self.patties}, Cheese: {self.cheese}, Tomato: {self.tomato}, Lettuce: {self.lettuce}, Cost: ${self.cost}'

# create all objects of burgers
byte_burger = Burger('Byte Burger','Milk', 'Tomato', 1, 0, 'no', 'yes', 'no', 5)
ctrl_alt_delicious = Burger('Ctrl-Alt-Delicious','Milk', 'Barbecue', 2, 2, 'yes', 'yes', 'yes', 11)
data_crunch = Burger('Data Crunch','Gluten free', 'Tomato', 0, 0, 'yes', 'yes', 'yes', 8)
code_cruncher = Burger('Code Cruncher','Milk', 'Tomato', 3, 3, 'yes', 'yes', 'yes', 15)

# function to change label
def change_label(burger, label):
    label.config(text=f"Burger Name: {burger.name} \n Type of Bun: {burger.bun} \n Type of Sauce: {burger.sauce}\n Number of Patties: {burger.patties} \n Number of Cheese Slices: {burger.cheese} \n Tomato: {burger.tomato} \n Lettuce: {burger.lettuce} \n Onion: {burger.onion} \n Cost: ${burger.cost}")

# window controls and config
burger_window = tk.Tk()
burger_window.resizable(width=False, height=False)
burger_window.title("Welcome to Codetown Burger")
label1 = tk.Label(burger_window, text=f"Burger Name: {byte_burger.name} \n Type of Bun: {byte_burger.bun} \n Type of Sauce: {byte_burger.sauce}\n Number of Patties: {byte_burger.patties} \n Number of Cheese Slices: {byte_burger.cheese} \n Tomato: {byte_burger.tomato} \n Lettuce: {byte_burger.lettuce} \n Onion: {byte_burger.onion} \n Cost: ${byte_burger.cost}", fg='black', bg='white')

# after 5 seconds, cycle to next burger option

# create buttons for each burger option
byte_button = tk.Button(burger_window, text="Byte Burger", fg='black', bg='white')
ctrl_button = tk.Button(burger_window, text="Ctrl-Alt-Delicious", fg='black', bg='white')
data_button = tk.Button(burger_window, text="Data Crunch", fg='black', bg='white')
code_button = tk.Button(burger_window, text="Code Cruncher", fg='black', bg='white')

# when clicked, show the burger details in a the current window
byte_button.bind("<Button-1>", lambda event: change_label(byte_burger, label1))
ctrl_button.bind("<Button-1>", lambda event: change_label(ctrl_alt_delicious, label1))
data_button.bind("<Button-1>", lambda event: change_label(data_crunch, label1))
code_button.bind("<Button-1>", lambda event: change_label(code_cruncher, label1))

# pack
label1.pack()
byte_button.pack(side=tk.LEFT)
ctrl_button.pack(side=tk.LEFT)
data_button.pack(side=tk.LEFT)
code_button.pack(side=tk.LEFT)
burger_window.mainloop()