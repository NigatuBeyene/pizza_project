import random


def size():
    global count
    pizza_size = {"s": 40,
                  "m": 50,
                  "l": 60,
                  "xl": 75}

    print(pizza_size)
    user = input("Enter pizza size: ")
    quantity = int(input("How much you need? "))
    count += pizza_size[user] * quantity
    return count


def extra():
    global count
    global spice
    extra_spice = input("Do you need extra? ")
    if extra_spice == "yes" or extra_spice == "y":
        count += spice
        return count
    else:
        return 0


def live():
    living = {
        "beersheva": 20,
        "b": 20,
        "a": 60,
        "another": 60}
    print(living)
    place = input("Where do you live? ")
    city = living[place]
    return city


