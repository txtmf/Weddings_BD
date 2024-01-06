class View:
    def __init__(self) -> None:
        pass

    def warn(self, message) -> None:
        print(f"{message}\n")

    def menu(self) -> str:
        print("1. Add client\n"
              "2. Add organizator\n"
              "3. Add place\n"
              "4. Add wedding\n"
              "5. Show clients\n"
              "6. Show organizators\n"
              "7. Show places\n"
              "8. Show weddings\n"
              "9. Update client\n"
              "10. Update organizator\n"
              "11. Update place\n"
              "12. Update wedding\n"
              "13. Delete client\n"
              "14. Delete organizator\n"
              "15. Delete place\n"
              "16. Delete wedding\n\n"
              "17. Generate batch\n\n"
              "18. Clients, their weddings in date range, and partners\n"
              "19. Organizator's weddings since\n"
              "20. Weddings at place since\n\n"
              "0. Quit\n")
        option = input("Option: ")
        print()
        return option
    
    def add_client(self) -> str:
        print("Add new client\n"
              'Example: "Mykolai Petrenko, +380980012354, mpetrenko@gmail.com"\n')
        arguments = input("Arguments: ")
        print()
        return arguments
    
    def show_clients(self, clients):
        print("Clients:")
        for client in clients:
            print(client)
        print()

    def update_client(self) -> str:
        print("Update existing client\n"
              'Example: "1, Mykolai Petrenko, +380980012354, mpetrenko@gmail.com"\n')
        arguments = input("Arguments: ")
        print()
        return arguments
    
    def delete_client(self) -> str:
        print("Delete existing client\n"
              'Example: "42"\n')
        arguments = input("ID: ")
        print()
        return arguments
    

    def add_organizator(self) -> str:
        print("Add new organizator\n"
              'Example: "Mykolai Petrenko, +380980012354, mpetrenko@gmail.com"\n')
        arguments = input("Arguments: ")
        print()
        return arguments
    
    def show_organizators(self, organizators):
        print("Organizators:")
        for organizator in organizators:
            print(f"ID: {organizator[0]}, Name: {organizator[1]}, Phone number: {organizator[2]}, Email: {organizator[3]}")
        print()

    def update_organizator(self) -> str:
        print("Update existing organizator\n"
              'Example: "1, Mykolai Petrenko, +380980012354, mpetrenko@gmail.com"\n')
        arguments = input("Arguments: ")
        print()
        return arguments
    
    def delete_organizator(self) -> str:
        print("Delete existing organizator\n"
              'Example: "42"\n')
        arguments = input("ID: ")
        print()
        return arguments


    def add_place(self) -> str:
        print("Add new place\n"
              'Example: "Vasil\'s, +380980012354, vasils_rest@gmail.com, 18 Velyka Vasylkivska street"\n')
        arguments = input("Arguments: ")
        print()
        return arguments
    
    def show_places(self, places):
        print("Places:")
        for place in places:
            print(f"ID: {place[0]}, Name: {place[1]}, Phone number: {place[2]}, Email: {place[3]}, Address: {place[4]}")
        print()

    def update_place(self) -> str:
        print("Update existing place\n"
              'Example: "1, Vasil\'s, +380980012354, vasils_rest@gmail.com, 18 Velyka Vasylkivska street"\n')
        arguments = input("Arguments: ")
        print()
        return arguments
    
    def delete_place(self) -> str:
        print("Delete existing place\n"
              'Example: "42"\n')
        arguments = input("ID: ")
        print()
        return arguments


    def add_wedding(self) -> str:
        print("Add new wedding\n"
              'Example: "Mykolai Petrenko, Oksana Kvach, 2024-04-12, 12:30, 23:00, 1, 1, 1"\n')
        arguments = input("Arguments: ")
        print()
        return arguments
    
    def show_weddings(self, weddings):
        print("Weddings:")
        for wedding in weddings:
            print(f"Partner1 name: {wedding[0]}, Partner2 name: {wedding[1]}, Date: {wedding[2]}, "
                  f"Start time: {wedding[3]}, End time: {wedding[4]}, "
                  f"Client ID: {wedding[5]}, Place ID: {wedding[6]}, Organizator ID: {wedding[7]}")
        print()

    def update_wedding(self) -> str:
        print("Update existing wedding\n"
              'Example: "Mykolai Petrenko, Oksana Kvach, 2024-04-12, 12:30, 23:00, 1, 1, 1"\n')
        arguments = input("Arguments: ")
        print()
        return arguments
    
    def delete_place(self) -> str:
        print("Delete existing wedding\n"
              'Example: "42"\n')
        arguments = input("Client ID: ")
        print()
        return arguments
    

    def generate_batch(self) -> str:
        print("Generate batch of clients, organizators, places, and weddings\n"
              'Example: "100000"\n')
        arguments = input("Rows: ")
        print()
        return arguments
    

    def client_date_partners_input(self) -> str:
        print("Show clients, date that they requested, and partners of the wedding\n"
              'Example: "2023-01-01, 2024-01-01"\n')
        arguments = input("Date range: ")
        print()
        return arguments
    
    def client_date_partners_output(self, table):
        for row in table:
            print(f"Client id: {row[0]}, Client name: {row[1]}, Date: {row[2]}, Partner 1 name: {row[3]}, Partner 2 name: {row[4]}")
        print()

    def organizator_weddings_input(self) -> str:
        print("Show organizators and the count of weddings they are organizing since date\n"
              'Example: "2023-01-01, 3"\n')
        arguments = input("Since date, minimum weddings count: ")
        print()
        return arguments
    
    def organizator_weddings_output(self, table):
        for row in table:
            print(f"Organizator id: {row[0]}, Name: {row[1]}, Phone number: {row[2]}, Email: {row[3]}, Weddings: {row[4]}")
        print()

    def weddings_place_input(self) -> str:
        print("Show weddings since date in a place, and the place itself\n"
              'Example: "2023-01-01"\n')
        arguments = input("Since date: ")
        print()
        return arguments
    
    def weddings_place_output(self, table):
        for row in table:
            print(f"Weddings: {row[0]}, Address: {row[1]}, Place: {row[2]}")
        print()