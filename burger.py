# class here for object creation
class Burger:
    def __init__(self, type_of_bun):
        self.bun = type_of_bun
        #self.sauce = sauce
        #self.cost = cost
    
    def __str__(self):
        return f'Type of Bun: {self.bun}' # extend this out
    
# data validation function. Will check for if the entries is one of the options for the input
def check_input(input_options, input_question):
    input_choice = input(input_question)
    if input_choice.lower() in input_options:
        return input_choice
    else:
        print('Not a valid option')
        check_input(input_options, input_question) # recursion means this will loop until valid option chosen

bun_options = ['milk','gluten free']
sauce_options = ['tomato', 'barbecue', 'none']

# costs for burger
plain_burger = 5
GF_bun = 1
add_patty = 3
extra_cheese_or_salad = 1

# store created burger objects
burger_array = []

# Menu
def menu():
    print('Welcome to Codetown Burger Co!')
    try: # data validation. Will error if they dont enter a number between 1 and 10
        burger_number = int(input('How many burgers would you like to order [1-10] \n'))
        if burger_number > 0 and burger_number <= 10:
            for number in range(burger_number):
                type_of_bun = check_input(bun_options, input_question=(f"What bun type should be included for Burger {number + 1}? {bun_options}? "))
                sauce = check_input(sauce_options, input_question=(f"What sauce should be included on Burger {number + 1}? {sauce_options}? "))
                #patties = check_input(patties_options, input_question=(f"How many patties should be on Burger {number + 1} [0-3]"))
                #slices_of_cheese = check_input(cheese_options, input_question=(f"How many slices of cheese should be on Burger {number + 1} [0-3]"))
                cost = 5
                if type_of_bun.lower() == 'gluten free':
                    cost += 1
            return burger_array.append(Burger(type_of_bun=type_of_bun))
        else:
            print('Please enter a number between 1 and 10')
            menu()
            
    except ValueError:
        print('Not a number. Please enter a number')
        menu()

#calculate the price of the burger and display it on screen
#include extras GF Bun = +$1, +patty = +$3, cheese or salad +$1

def start_app():
    menu()
    for burger in burger_array:
        print(burger)

if __name__ == '__main__':
    start_app()