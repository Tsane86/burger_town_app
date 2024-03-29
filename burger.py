# class here for object creation
class Burger:
    def __init__(self, type_of_bun, sauce, patties, cheese, tomato, lettuce, onion, cost):
        self.bun = type_of_bun
        self.sauce = sauce
        self.patties = patties
        self.cheese = cheese
        self.tomato = tomato
        self.lettuce = lettuce
        self.onion = onion
        self.cost = cost
    
    def __str__(self):
        return f'Type of Bun: {self.bun}, Sauce: {self.sauce}, Patties: {self.patties}, Cheese: {self.cheese}, Tomato: {self.toamto}, Lettuce: {self.lettuce}, Onion: {self.onion}, Cost: {self.cost}' # extend this out
    
# data validation function. Will check for if the entries is one of the options for the input question.
def check_input(input_options, input_question):
    input_choice = input(input_question)
    if input_choice.lower() in input_options:
        return input_choice
    else:
        print(f'Not a valid option. Please enter a valid option: {input_options}')
        check_input(input_options, input_question) # recursion means this will loop until valid option chosen

def calculate_burger_cost(type_of_bun, patties, slices_of_cheese, has_lettuce, has_onion, has_tomato):
    cost = 5
    if type_of_bun.lower() == 'gluten free':
        cost += 1
    if patties > 1:
        cost += (3*(patties-1))
    if slices_of_cheese > 1:
        cost += (1*(slices_of_cheese-1))
    salad_options = [has_lettuce, has_onion, has_tomato]
    number_of_salad_items = 0
    for salad in salad_options:
        if salad == 'yes':
            number_of_salad_items += 1
    if number_of_salad_items > 1:
       cost += (1*(number_of_salad_items-1)) 
    return cost #TODO test this
        

# options for user input
bun_options = ['milk', 'gluten free']
sauce_options = ['tomato', 'barbecue', 'none']
patties_options = cheese_options = ['0', '1', '2' , '3']
tomato_options = lettuce_options = onion_options = ['yes','no']
#TODO add more options

# costs for burger
plain_burger = 5
GF_bun = 1
add_patty = 3
extra_cheese_or_salad = 1

# store created burger objects
burger_array = []

# function to total cost
def calculate_total_cost(burger_array):
    total_cost = 0
    for burger in burger_array:
        total_cost += burger.cost
    return total_cost
#TODO check this works

# Menu
def menu():
    print('Welcome to Codetown Burger Co!')
    try: # data validation. Will error if they dont enter a number between 1 and 10
        burger_number = int(input('How many burgers would you like to order [1-10] \n'))
        if burger_number > 0 and burger_number <= 10:
            for number in range(burger_number):
                type_of_bun = check_input(bun_options, input_question=(f"What bun type should be included for Burger {number + 1}? {bun_options}? "))
                sauce = check_input(sauce_options, input_question=(f"What sauce should be included on Burger {number + 1}? {sauce_options}? "))
                patties = check_input(patties_options, input_question=(f"How many patties should be on Burger {number + 1} [0-3]? "))
                slices_of_cheese = check_input(cheese_options, input_question=(f"How many slices of cheese should be on Burger {number + 1} [0-3]? "))
                has_tomato = check_input(tomato_options, input_question=(f"Should Burger {number + 1} have tomato {tomato_options}? "))
                has_lettuce = check_input(lettuce_options, input_question=(f"Should Burger {number + 1} have lettuce {lettuce_options}? "))
                has_onion = check_input(onion_options, input_question=(f"Should Burger {number + 1} have onion {onion_options}? "))
                cost = 5
                #TODO cost calculator, might be easier as a function. input will need to be type of bun,

                
            return burger_array.append(Burger(type_of_bun=type_of_bun, sauce=sauce, patties=patties, cheese=slices_of_cheese, tomato=has_tomato, lettuce=has_lettuce, onion=has_onion, cost=cost))
        else:
            print('Please enter a number between 1 and 10')
            menu()
            
    except ValueError:
        print('Not a number. Please enter a number')
        menu()

def start_app():
    menu()
    print(burger_array)

if __name__ == '__main__':
    start_app()