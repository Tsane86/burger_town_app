# class here for object creation
class Burger:
    def __init__(self, type_of_bun, sauce, cost):
        self.bun = type_of_bun
        self.sauce = sauce
        self.cost = cost
    
    def __str__(self):
        return f'Type of Bun: {self.bun}, Cost: {self.cost}' # extend this out
    
# data validation function. Will check for if the entries is one of the options for the input
def check_input(input, input_options):
    return input.lower() in input_options #this will return true or false, which can then be used in a conditional

input_options =['milk','gluten free','tomato','bbq']

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
                type_of_bun = input(f'What bun type should be included for Burger {number + 1}? Milk or Gluten Free? \n')
                if check_input(type_of_bun, input_options) != True:
                    print('Please double check your entry')
                    menu()
                sauce = input(f'What sauce should be included on Burger {number}? Tomato, BBQ or None? \n')
                if check_input(sauce, input_options) != True:
                    print('Please double check your entry')
                    menu()
                cost = 5
                if type_of_bun.lower() == 'gluten free':
                    cost += 1
                return burger_array.append(Burger(type_of_bun=type_of_bun, sauce=sauce, cost=cost))
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