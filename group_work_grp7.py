from collections import deque


class Event:
    def __init__(self, eventId, eventName, Date, seat_available, location):
        self.Id = eventId
        self.name = eventName
        self.Date = Date
        self.location = location
        self.seats = seat_available


viewEvents = [["ID", "|", "eventName", "|", "Date", "|", "seats", "|", "location"]]


class Ticket:
    def __init__(self, eventId, bookedCustomer, price=1000):
        self.eventId = eventId
        self.customer = bookedCustomer
        self.price = price


viewTicketCustomer = [["eventId", "|" ,"bookedCustomer", "|" ,"price"]]

class EventTicketingSystem:
    def __init__(self):
        self.events = []
        self.eventBooked_tickets = deque()
        self.handling_tickets_cancellation = []

    def add_event(self, eventId, eventName, Date, seat_available, location):
        event = Event(eventId, eventName, Date, seat_available, location)
        self.events.append(event)
        duplicate = [eventId, "|", eventName,
                    "|", Date, "|", seat_available, "|", location]
        viewEvents.append(duplicate)
        
    def viewEvents(self):
        print("{:<10}".format("All Events purchased with customers"))
        print("------------------------------------------------------------------------------------------")
        for event in viewEvents:
           print("{:<20} {:<3} {:<20} {:<3} {:<20} {:<3} {:<5} {:<3} {:20}".format(*event))
        print("------------------------------------------------------------------------------------------")
           
    def book_ticket(self, eventId, customerName):
        for event in self.events:
            if event.Id == eventId:
                if event.seats:
                    ticket = Ticket(eventId, customerName)
                    self.eventBooked_tickets.append(ticket)
                    event.seats -= 1
                    duplicate = [eventId, "|", customerName, "|", 1000]
                    viewTicketCustomer.append(duplicate)
                    return True
                else:
                    print('no seats remain')
                    return False
        else:
            print("This event is not available")
            return False
    def viewAllTickets(self):
        print("{:<30}".format('All ticket purchased with customers'))
        
        print("-------------------------------------------------------")
        
        for ticket in viewTicketCustomer:
           print("{:<20} {:<3} {:<20} {:<3} {:5}".format(*ticket))
    
        print("-------------------------------------------------------")
    def ticket_cancellation(self):
        canceled_ticket = self.eventBooked_tickets.popleft()
        viewTicketCustomer.pop(1)
        for event in self.events:
            if event.Id == canceled_ticket.eventId:
                event.seats += 1
                break
        self.handling_tickets_cancellation.append(canceled_ticket)
        print(f"The ticket of {canceled_ticket.customer} is cancelled")
        return True

    def refund(self):
        reduction = 1000 - (1000 * 10 / 100)
        print(f"The {self.handling_tickets_cancellation[-1].customer} is refunded {reduction} $")
        return reduction


eventTicketingSystem = EventTicketingSystem()

eventTicketingSystem.add_event(1, "Iwacu musica", "23/08/2022", 1, "kigali")
eventTicketingSystem.add_event(2, "cocacola", "20/07/2020", 20, "Huye")
eventTicketingSystem.add_event(3, "youthConnect", "2/06/2024", 20, "musanze")
eventTicketingSystem.add_event(4, "umuganura", "23/05/2026", 20, "kigali")
eventTicketingSystem.add_event(5, "kwibohora", "23/04/2027", 20, "huye")
eventTicketingSystem.add_event(6, "induction", "23/02/2022", 20, "musanze")
eventTicketingSystem.add_event(7, "FIFA", "23/03/2023", 20, "huye")
eventTicketingSystem.add_event(8, "Aper comfrence", "23/05/2025", 20, "kigali")
eventTicketingSystem.add_event(9, "Talent show", "23/07/2026", 20, "musanze")
eventTicketingSystem.add_event(10, "King show", "23/06/2023", 20, "kigali")
eventTicketingSystem.add_event(11, "Iwacu musica", "23/08/2022", 1, "kigali")
eventTicketingSystem.add_event(12, "cocacola", "20/07/2020", 20, "Huye")
eventTicketingSystem.add_event(13, "youthConnect", "2/06/2024", 20, "musanze")
eventTicketingSystem.add_event(14, "umuganura", "23/05/2026", 20, "kigali")
eventTicketingSystem.add_event(15, "kwibohora", "23/04/2027", 20, "huye")
eventTicketingSystem.add_event(16, "induction", "23/02/2022", 20, "musanze")
eventTicketingSystem.add_event(17, "FIFA", "23/03/2023", 20, "huye")
eventTicketingSystem.add_event(18, "Aper comfrence", "23/05/2025", 20, "kigali")
eventTicketingSystem.add_event(19, "Talent show", "23/07/2026", 20, "musanze")
eventTicketingSystem.add_event(20, "King show", "23/06/2023", 20, "kigali")
eventTicketingSystem.viewEvents()

eventTicketingSystem.book_ticket(1, "claude")
eventTicketingSystem.book_ticket(6, "alayn")
eventTicketingSystem.book_ticket(8, "kenny")
eventTicketingSystem.book_ticket(20, "dior")
eventTicketingSystem.book_ticket(3, "claude")
eventTicketingSystem.book_ticket(4, "Patrick")
eventTicketingSystem.book_ticket(5, "iranzi")
eventTicketingSystem.book_ticket(9, "bahati")
eventTicketingSystem.book_ticket(1, "uwera")
eventTicketingSystem.book_ticket(1, "claude")
eventTicketingSystem.book_ticket(6, "alayn")
eventTicketingSystem.book_ticket(8, "kenny")
eventTicketingSystem.book_ticket(20, "dior")
eventTicketingSystem.book_ticket(3, "claude")
eventTicketingSystem.book_ticket(4, "Patrick")
eventTicketingSystem.book_ticket(5, "iranzi")
eventTicketingSystem.book_ticket(9, "bahati")
eventTicketingSystem.book_ticket(1, "uwera")

eventTicketingSystem.viewAllTickets()

eventTicketingSystem.ticket_cancellation()
eventTicketingSystem.refund()
eventTicketingSystem.book_ticket(1, "after the one cancel")
eventTicketingSystem.viewAllTickets()

def ask_yes_no(question):
    while True:
        response = input(question + " (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Please answer with 'yes' or 'no'.")


def EventQuestions(number):
    while number < 3:
        question1 = ask_yes_no("are you an admin ")
        if question1 == "yes":
            question2 = ask_yes_no("Do you want to add an event ")
            if (question2 == "yes"):
                eventName = input("enter event eventName: ").strip().lower()
                Date = input("enter event Date: ").strip().lower()
                location = input("enter event location: ").strip().lower()
                seat_available = int(
                    input("enter event seat_available: ").strip().lower())
                eventTicketingSystem.add_event(
                    number, eventName, Date, seat_available, location)
        if question1 == "no":
            return False
        number += 1
    eventTicketingSystem.viewEvents()

def bookQuestions(number):
    while number < 2:
        book = ask_yes_no("Do you want to book ticket? ")
        if (book == "yes"):
            id = int(input('Write event id: ').strip().lower())
            customer = input('Write your name: ').strip().lower()
            eventTicketingSystem.book_ticket(id, customer)
            number += 1
        else:
            number += 1
    return True


def review(number):
    if bookQuestions(1):
        eventTicketingSystem.viewAllTickets()
        while number < 3:
            answer = ask_yes_no("do you want to cancel your ticket ? ")
            if (answer == "yes"):
                cancel = eventTicketingSystem.ticket_cancellation()
                canceledTicket = eventTicketingSystem.handling_tickets_cancellation[-1]
                for ticket in viewTicketCustomer:
                    if canceledTicket.eventId in ticket:
                        viewTicketCustomer.remove(ticket)
                    break
                reduction = eventTicketingSystem.refund()
                print(f"You {canceledTicket.customer} have been refunded {reduction} $")
                if (cancel):
                    bookQuestions(20)
                number += 1
            else:
                print("Thank you !")
                break


def last():
    if not EventQuestions(1):
        print("time for customer booking tickets")
        bookQuestions(1)
    print("Time for review tickets to customers")
    review(1)

last()
