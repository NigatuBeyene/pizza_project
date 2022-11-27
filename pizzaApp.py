from pizzaMain import size
from pizzaMain import extra
from pizzaMain import live
from pizzaUtility import game

spice = 2
count = 0


def pizza():

    net = 0
    age = int(input("Enter your age: "))
    if age >= 18:
        print("\n\n\t\t\t\t\t\t\t**** WELLCOME TO OUR PIZZA *****\n\n")
        net += size() + extra()
        total_net = (net + live())
        total_net_discount = (total_net - game())
        con = input("Do you want to continue? ")
        if con == "no" or con == "n":
            print("Total price is: ", total_net)
            print("Total price after discount: ", round(total_net_discount, 2))
            print("*********THANKS YOUR BUYING!!!****** ")

        else:
            while True:
                net += size() + extra()
                con = input("Do you want to continue? ")
                if con == "no" or con == "n":
                    print("Total price is: ", total_net)
                    print("Total price after discount: ", round(total_net_discount, 2))
                    print("*********THANKS YOUR BUYING!!!****** ")
                    break

    else:
        print("sorry, your are under age!")


pizza()




