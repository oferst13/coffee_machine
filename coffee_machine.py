class CoffeeMachine:
    def __init__(self):
        self.state = "ready"
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.cash = 550

    def user_input(self, push):
        if self.state == "ready":
            if push == "buy":
                self.buy()
            elif push == "fill":
                self.fill()
            elif push == "take":
                self.take()
            elif push == "remaining":
                self.remaining()

    def buy(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee_type == "1":
            req_water = 250
            req_milk = 0
            req_beans = 16
            price = 4
        elif coffee_type == "2":
            req_water = 350
            req_milk = 75
            req_beans = 20
            price = 7
        elif coffee_type == "3":
            req_water = 200
            req_milk = 100
            req_beans = 12
            price = 6
        else:
            return
        if self.water - req_water < 0:
            print("Sorry, not enough water!")
            return
        if self.milk - req_milk < 0:
            print("Sorry, not enough milk!")
            return
        if self.beans - req_beans < 0:
            print("Sorry, not enough coffee beans!")
            return
        if self.cups - 1 < 0:
            print("Sorry, not enough disposable cups!")
            return
        print("I have enough resources, making you a coffee!")
        self.water -= req_water
        self.milk -= req_milk
        self.beans -= req_beans
        self.cups -= 1
        self.cash += price

    def fill(self):
        water = int(input("Write how many ml of water do you want to add:"))
        milk = int(input("Write how many ml of milk do you want to add:"))
        beans = int(input("Write how many grams of coffee beans do you want to add:"))
        cups = int(input("Write how many disposable cups do you want to add:"))
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def take(self):
        print("I gave you ${}".format(self.cash))
        self.cash = 0

    def remaining(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("{} of money".format(self.cash))


def main():
    machine = CoffeeMachine()
    action = input("Write action (buy, fill, take, remaining, exit):")
    while action != "exit":
        machine.user_input(action)
        action = input("Write action (buy, fill, take, remaining, exit):")


main()
