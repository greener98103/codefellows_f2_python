#!/usr/bin/env python

fruits = [u"Apples", u"Pears", u"Oranges", u"Peaches"]

def print_fruits(fruits):
    """Print all fruits in the sequence"""
    for fruit in fruits:
        print fruit    

def get_fruit(prompt):
    """Get the name of another fruit."""
    while True:
        fruit_in = raw_input(prompt)
        if fruit_in.isalpha():
            break
        else:
            print(u"Letters only please.")

    return unicode(fruit_in)

def get_num(max_num):
    """Get a number in the range of 1 to passed parameter"""
    while True:
        num_in = raw_input(u"\nEnter a number between 1 and {}: ".format(max_num))
        if num_in.isdigit():
            num_in = int(num_in)
            if num_in >= 1 and num_in <= max_num:
                break
            else:
                print u"Please limit your entry to the range specified."
        else:
            print u"Numbers only please."

    return num_in

# list_lab series 1
print_fruits(fruits)
fruits.extend([get_fruit(u"\nPlease add another fruit to the list: ")])
print_fruits(fruits)

fruit_num = get_num(len(fruits))
print u"Fruit number {} is {}.".format(fruit_num, fruits[fruit_num - 1])

one_fruit = [get_fruit(u"\nPlease add another fruit to the list: ")]
fruits = one_fruit + fruits
print_fruits(fruits)

one_fruit = get_fruit(u"\nPlease add another fruit to the list: ")
fruits.insert(0, one_fruit)
print_fruits(fruits)

print u"\nThese fruits begin with 'P':"
for fruit in fruits:
    if fruit[0] == 'P':
        print fruit

# list_lab series 2

