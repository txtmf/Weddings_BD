from Model import *
from View import *
import datetime as dt

def is_email(string: str) -> bool:
    if len(string) > 255:
        return False
    if string[0] == '@' or string.count('@') != 1:
        return False
    if string.split('@')[1][0] == '.' or string.split('@')[1].count('.') < 1:
        return False
    for part in string.split('@')[1].split('.'):
        if len(part) == 0 or part[0].isdigit():
            return False
    return True

def is_date(string: str) -> bool:
    try:
        dt.datetime.strptime(string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_time(string: str) -> bool:
    try:
        dt.datetime.strptime(string, '%H:%M')
        return True
    except ValueError:
        return False

def is_phone_number(string: str) -> bool:
    if string[:4] != "+380" or len(string) != 13:
        return False
    if not string[4:].isdigit():
        return False
    return True

def is_name(string: str) -> bool:
    if len(string) > 256 or len(string) == 0 or not string.replace(' ', '').isalpha():
        return False
    return True

def is_address(string: str) -> bool:
    if len(string) > 256 or len(string) == 0:
        return False
    return True

class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View()

    def validate(self, name = None, phone_number = None, email = None,
                 address = None, partner1_name = None, partner2_name = None,
                 date = None, start_time = None, end_time = None):
        if name is not None and not is_name(name):
            self.view.warn("Bad name")
            return False
        if partner1_name is not None and not is_name(partner1_name):
            self.view.warn("Bad partner1 name")
            return False
        if partner2_name is not None and not is_name(partner2_name):
            self.view.warn("Bad partner2 name")
            return False
        if phone_number is not None and not is_phone_number(phone_number):
            self.view.warn("Bad phone number")
            return
        if email is not None and not is_email(email):
            self.view.warn("Bad email")
            return
        if date is not None and not is_date(date):
            self.view.warn("Bad date")
            return
        if start_time is not None and not is_time(start_time):
            self.view.warn("Bad start time")
            return
        if end_time is not None and not is_time(end_time):
            self.view.warn("Bad end time")
            return
        if address is not None and not is_address(address):
            self.view.warn("Bad address")
            return
        return True

    def main(self):
        options = {'1' : self.add_client, '2' : self.add_organizator, '3' : self.add_place, '4' : self.add_wedding,
                   '5' : self.show_clients, '6' : self.show_organizators, '7' : self.show_places, '8' : self.show_weddings,
                   '9' : self.update_client, '10' : self.update_organizator, '11' : self.update_place, '12' : self.update_wedding,
                   '13' : self.delete_client, '14' : self.delete_organizator, '15' : self.delete_place, '16' : self.delete_wedding,
                   '17' : self.generate_batch, '18' : self.client_date_partners, '19' : self.organizator_weddings, '20' : self.weddings_place}
        while True:
            option = self.view.menu().strip()

            if option == '0':
                break

            if option in options:
                options[option]()
            else:
                self.view.warn("Wrong option!")

    def add_client(self):
        arguments = self.view.add_client()
        try:
            name, phone_number, email = [arg.strip() for arg in arguments.split(",")]
        except:
            self.view.warn("Bad input")
            return
        if not self.validate(name, phone_number, email):
            return
        self.model.add_client(name, phone_number, email)
    
    def show_clients(self):
        self.view.show_clients(self.model.get_all_clients())

    def update_client(self):
        arguments = self.view.update_client()
        try:
            id, name, phone_number, email = [arg.strip() for arg in arguments.split(",")]
        except:
            self.view.warn("Bad input")
            return
        try:
            id = int(id)
            if self.model.get_client(id) is None:
                self.view.warn("ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad ID")
            return
        if not self.validate(name, phone_number, email):
            return
        self.model.update_client(id, name, phone_number, email)

    def delete_client(self):
        arguments = self.view.delete_client()
        id = arguments.strip()
        try:
            id = int(id)
            if self.model.get_client(id) is None:
                self.view.warn("ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad ID")
            return
        self.model.delete_client(id)


    def add_organizator(self):
        arguments = self.view.add_organizator()
        try:
            name, phone_number, email = [arg.strip() for arg in arguments.split(",")]
        except:
            self.view.warn("Bad input")
            return
        if not self.validate(name, phone_number, email):
            return
        self.model.add_organizator(name, phone_number, email)

    def show_organizators(self):
        self.view.show_organizators(self.model.get_all_organizators())

    def update_organizator(self):
        arguments = self.view.update_organizator()
        try:
            id, name, phone_number, email = [arg.strip() for arg in arguments.split(",")]
        except:
            self.view.warn("Bad input")
            return
        try:
            id = int(id)
            if len(self.model.get_organizator(id)) == 0:
                self.view.warn("ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad ID")
            return
        if not self.validate(name, phone_number, email):
            return
        self.model.update_organizator(id, name, phone_number, email)

    def delete_organizator(self):
        arguments = self.view.delete_organizator()
        id = arguments.strip()
        try:
            id = int(id)
            if len(self.model.get_organizator(id)) == 0:
                self.view.warn("ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad ID")
            return
        self.model.delete_organizator(id)


    def add_place(self):
        arguments = self.view.add_place()
        try:
            name, phone_number, email, address = [arg.strip() for arg in arguments.split(",")]
        except:
            self.view.warn("Bad input")
            return
        if not self.validate(name = name, phone_number = phone_number, email = email, address = address):
            return
        self.model.add_place(name, phone_number, email, address)

    def show_places(self):
        self.view.show_places(self.model.get_all_places())

    def update_place(self):
        arguments = self.view.update_place()
        try:
            id, name, phone_number, email, address = [arg.strip() for arg in arguments.split(",")]
        except:
            self.view.warn("Bad input")
            return
        try:
            id = int(id)
            if len(self.model.get_place(id)) == 0:
                self.view.warn("ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad ID")
            return
        if not self.validate(name = name, phone_number = phone_number, email = email, address = address):
            return
        self.model.update_place(id, name, phone_number, email, address)

    def delete_place(self):
        arguments = self.view.delete_place()
        id = arguments.strip()
        try:
            id = int(id)
            if len(self.model.get_place(id)) == 0:
                self.view.warn("ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad ID")
            return
        self.model.delete_place(id)


    def add_wedding(self):
        arguments = self.view.add_wedding()
        try:
            partner1_name, partner2_name, \
            date, start_time, end_time, \
            client_id, place_id, organizator_id = [arg.strip() for arg in arguments.split(",")]
        except:
            self.view.warn("Bad input")
            return
        try:
            client_id = int(client_id)
            if len(self.model.get_client(client_id)) == 0:
                self.view.warn("Client ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad Client ID")
            return
        try:
            place_id = int(place_id)
            if len(self.model.get_place(place_id)) == 0:
                self.view.warn("Place ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad Place ID")
            return
        try:
            organizator_id = int(organizator_id)
            if len(self.model.get_organizator(organizator_id)) == 0:
                self.view.warn("Organizator ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad Organizator ID")
            return
        if not self.validate(partner1_name = partner1_name, partner2_name = partner2_name,
                             date = date, start_time = start_time, end_time = end_time):
            return
        self.model.add_wedding(partner1_name, partner2_name,
                              date, start_time, end_time,
                              client_id, place_id, organizator_id)
        
    def show_weddings(self):
        self.view.show_weddings(self.model.get_all_weddings())

    def update_wedding(self):
        arguments = self.view.update_wedding()
        try:
            partner1_name, partner2_name, \
            date, start_time, end_time, \
            client_id, place_id, organizator_id = [arg.strip() for arg in arguments.split(",")]
        except:
            self.view.warn("Bad input")
            return
        try:
            client_id = int(client_id)
            if len(self.model.get_client(client_id)) == 0:
                self.view.warn("Client ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad Client ID")
            return
        try:
            place_id = int(place_id)
            if len(self.model.get_place(place_id)) == 0:
                self.view.warn("Place ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad Place ID")
            return
        try:
            organizator_id = int(organizator_id)
            if len(self.model.get_organizator(organizator_id)) == 0:
                self.view.warn("Organizator ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad Organizator ID")
            return
        if not self.validate(partner1_name = partner1_name, partner2_name = partner2_name,
                             date = date, start_time = start_time, end_time = end_time):
            return
        self.model.update_wedding(partner1_name, partner2_name, date, start_time, end_time,
                                  client_id, place_id, organizator_id)
        
    def delete_wedding(self):
        arguments = self.view.delete_wedding()
        id = arguments.strip()
        try:
            id = int(id)
            if len(self.model.get_wedding(id)) == 0:
                self.view.warn("ID doesn't exist")
                return
        except:
            self.view.warn(f"Bad ID")
            return
        self.model.delete_wedding(id)


    def generate_batch(self):
        arguments = self.view.generate_batch()
        try:
            rows = int(arguments.strip())
        except:
            self.view.warn(f"Bad number of rows")
            return
        if rows <= 0:
            self.view.warn(f"Number should be greater or equal to 1")
            return
        try:
            exec_time = self.model.generate_batch(rows)
        except psycopg2.errors.UniqueViolation as uv:
            self.view.warn("Unique constraint violation due to randomness!\n"
                           "Try less rows or clean the table")
            self.view.warn(uv)
        except Exception as e:
            self.view.warn("Generation is aborted")
            self.view.warn(e)
        self.view.warn(f'Generated {rows} rows in {exec_time / (10**6)} ms')

    
    def client_date_partners(self):
        arguments = self.view.client_date_partners_input()
        try:
            left_date, right_date = [arg.strip() for arg in arguments.split(",")]
        except:
            self.view.warn("Bad input")
            return
        if not self.validate(date=left_date) or not self.validate(date=right_date):
            self.view.warn("Bad date")
            return
        if dt.datetime.strptime(left_date, '%Y-%m-%d') > dt.datetime.strptime(right_date, '%Y-%m-%d'):
            temp = left_date
            left_date = right_date
            right_date = temp
        table, exec_time = self.model.client_date_partners(left_date, right_date)
        self.view.warn(f'Query execution time is {exec_time / (10**6)} ms')
        self.view.client_date_partners_output(table)

    def organizator_weddings(self):
        arguments = self.view.organizator_weddings_input()
        try:
            date, min_weddings = [arg.strip() for arg in arguments.split(',')]
        except:
            self.view.warn("Bad input")
        if not self.validate(date=date):
            self.view.warn("Bad date")
            return
        try:
            min_weddings = int(min_weddings)
            if min_weddings < 0:
                self.view.warn("Bad minimum. Must be at least 0")
                return
        except:
            self.view.warn("Bad number")
            return
        table, exec_time = self.model.organizator_weddings(date, min_weddings)
        self.view.warn(f'Query execution time is {exec_time / (10**6)} ms')
        self.view.organizator_weddings_output(table)

    def weddings_place(self):
        arguments = self.view.weddings_place_input()
        date = arguments.strip()
        if not self.validate(date=date):
            self.view.warn("Bad date")
            return
        table, exec_time = self.model.weddings_place(date)
        self.view.warn(f'Query execution time is {exec_time / (10**6)} ms')
        self.view.weddings_place_output(table)