# Codetown Burger Co App V1

# read in orders.txt
def read_orders(order_text_file):
    with open(order_text_file, 'r') as file:
        orders = file.readlines()
    return orders

# convert each list item to a tuple
def convert_to_tuple(orders):
    tuples = []
    for order in orders:
        order = order.strip('\n')
        tuples.append(tuple(order.split(',')))
    return tuples

# create a dictionary based on the Tuple as the Keys
def create_burger_dict(tuples):
    my_dict = {}
    for order in tuples:
        my_dict[order] = 0
    return my_dict

# count the numbers of options in the Tuple and add the counts to the dictionary
def count_burgers(tuples, dictionary):
    for order in tuples:
        dictionary[order] += 1
    return dictionary

# sort the counts in the dictionary
def sort_burger_dict(dictionary):
    sort_dict = dict(sorted(dictionary.items(), key=lambda item:item[1]))
    return sort_dict

# costs for burger
plain_burger = 5
GF_bun = 1
add_patty = 3
extra_cheese_or_salad = 1

# calculate burger costs
def get_cost(burger):
    cost = 5
    if burger[0].lower() == 'gluten free':
        cost += 1
    if int(burger[2]) > 1:
        number_of_additional_patties = int(burger[2]) - 1
        cost += (3*number_of_additional_patties)
    if int(burger[3]) > 1:
        number_of_additional_cheese_slices = int(burger[3]) - 1
        cost += number_of_additional_cheese_slices
    salad_options = [burger[4], burger[5], burger[6]]
    number_of_salad_items = 0
    for salad in salad_options:
        if salad == 'yes':
            number_of_salad_items += 1
    if number_of_salad_items > 1:
        cost += (1*(number_of_salad_items-1))
    return cost

# print burger option and cost
def top_burgers_cost(sorted_burgers):
    top_burgers = []
    for key, value in sorted_burgers.items():
        value_string = (f'{key} - {value} - ${get_cost(key)}')
        top_burgers.append(value_string)
    return top_burgers

# application start
def start_app():
    orders = read_orders('orders.txt')
    tuples = convert_to_tuple(orders)
    burger_dictionary = create_burger_dict(tuples)
    counted_burgers = count_burgers(tuples, burger_dictionary)
    sorted_burgers = sort_burger_dict(counted_burgers)
    input_number = int(input('How many top burgers would you like to output? \n'))
    top_burgers = top_burgers_cost(sorted_burgers)
    for burger in top_burgers[:input_number]:
        print(burger)

if __name__ == '__main__':
    start_app()