class ParkingGarage():

# METHODS:
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self, minusTicket = 1, minusParkingSpace = 1):
        if self.tickets[0] > 0:
            # decrease the amount of tickets available by 1
            self.tickets[0] -= minusTicket
            # decrease the amount of parkingSpaces available by 1
            self.parkingSpaces[0] -= minusParkingSpace
            print("Thank you for choosing our parking garage! \nPlease take your ticket ->")
            # ***to double check number of available tickets and parking spaces***
            # print(self.tickets[0])
            # print(self.parkingSpaces[0])
        elif self.tickets[0] <= 0:
            self.tickets[0] = 0
            self.parkingSpaces[0] = 0
            print("We're sorry! Our garage is currently full. Please try us again later!")
            # print(self.tickets[0])
            # print(self.parkingSpaces[0])

    def payForParking(self):
        # display an input() that waits for an amount from the user and store it in a variable ---> 
        payment = input("Please add your payment amount here: ")
        # ***Trying to find a way to only accept integers as inputs without breaking the rest of my code***
        # ***while True:
        #     if payment.isdigit():
        #         return
        #     else:
        #         print("Please input amount using digits only.")
        #         payment = input("Please add your payment amount here: ")***
        
        while True:
            if len(payment) == 0:
                my_garage.currentTicket['paid'] = False
                print("Your ticket has not been paid. Please pay for your ticket.")
                payment = input("Please add your payment amount here: ")
            elif len(payment) != 0:
                # This should update the 'currentTicket' dictionary key "paid" to True
                my_garage.currentTicket['paid'] = True
                # if the payment variable is not empty (meaning the ticket has been paid), then display a message to the user that their ticket has been paid and they have 15mins to leave 
                print("Your ticket has been paid. You have 15 minutes to exit the garage.")
                # while payment != payment.isdigit():
                #     print("Please input amount using digits only.")
                #     payment = input("Please add your payment amount here: ")
                # while payment == payment.isdigit():
                #     pass
                return

    
    def leaveGarage(self, plusTicket = 1, plusParkingSpace = 1):
        # If the ticket has been paid, display a message of "Thank You, have a nice day."
        if my_garage.currentTicket['paid'] == True:
            print("Thank you, have a nice day!")
        if my_garage.currentTicket['paid'] != True:
            return
        if self.tickets[0] <= 25:
            # Update tickets list to increase by 1 (Add to the list)
            self.tickets[0] += plusTicket
            # Update parkingSpaces list to increase by 1 (add to the list)
            self.parkingSpaces[0] += plusParkingSpace
        if self.tickets[0] > 25:
            self.tickets[0] = 25
            self.parkingSpaces[0] = 25
            # ***trying to find a way to prevent users from leaving the garage "without a ticket" (when all parking spaces are open, thus no tickets were "given out")
            #  ***print("You do not have a ticket. Please take a ticket upon entering the garage. ")
        print(self.tickets[0])
        print(self.parkingSpaces[0])

# ATTRIBUTES:
    # tickets = []
    # parkingSpaces = []
    # currentTicket = {}

my_garage = ParkingGarage([25], [25], {'paid': False})

def run():
    while True: 
        status = input("Are you entering or exiting? ")

        if status.lower() == 'entering':
            my_garage.takeTicket()
        elif status.lower() == 'exiting':
            my_garage.payForParking()
            my_garage.leaveGarage()
        else:
            print("Please choose 'entering' or 'exiting'")

run()