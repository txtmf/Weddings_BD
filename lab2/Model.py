import time
import datetime as dt
import psycopg2
from typing import List
from sqlalchemy import ForeignKey, String, BigInteger, Date, Time
from sqlalchemy import create_engine
from sqlalchemy import select, update, delete
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class Client(Base):
    __tablename__ = "Clients"
    
    id: Mapped[int] = mapped_column(BigInteger, primary_key = True)
    name: Mapped[str] = mapped_column(String(256))
    phone_number: Mapped[str] = mapped_column(String(16))
    email: Mapped[str] = mapped_column(String(255))

    wedding: Mapped['Wedding'] = relationship(back_populates = 'client')

    def __repr__(self):
        return f'Client(id: {self.id}, name: {self.name}, phone_number: {self.phone_number}, email: {self.email})'

class Organizator(Base):
    __tablename__ = "Organizators"
    
    id: Mapped[int] = mapped_column(BigInteger, primary_key = True)
    name: Mapped[str] = mapped_column(String(256))
    phone_number: Mapped[str] = mapped_column(String(16), unique = True)
    email: Mapped[str] = mapped_column(String(255), unique = True)

    weddings: Mapped[List['Wedding']] = relationship(back_populates = 'organizator')
    
    def __repr__(self):
        return f'Organizator(id: {self.id}, name: {self.name}, phone_number: {self.phone_number}, email: {self.email})'

class Place(Base):
    __tablename__ = "Places"

    id: Mapped[int] = mapped_column(BigInteger, primary_key  =True)
    name: Mapped[str] = mapped_column(String(256))
    phone_number: Mapped[str] = mapped_column(String(16), unique = True)
    email: Mapped[str] = mapped_column(String(255), unique = True)
    address: Mapped[str] = mapped_column(String(128))

    weddings: Mapped[List['Wedding']] = relationship(back_populates = 'place')

    def __repr__(self):
        return f'Place(id: {self.id}, name: {self.name}, phone_number: {self.phone_number}, email: {self.email})'

class Wedding(Base):
    __tablename__ = "Weddings"

    client_id = mapped_column(ForeignKey('Clients.id'), primary_key = True)
    organizator_id = mapped_column(ForeignKey('Organizators.id'))
    place_id = mapped_column(ForeignKey('Places.id'))

    partner1_name: Mapped[str] = mapped_column(String(256))
    partner2_name: Mapped[str] = mapped_column(String(256))
    date: Mapped[dt.date] = mapped_column(Date)
    start_time: Mapped[dt.time] = mapped_column(Time)
    end_time: Mapped[dt.time] = mapped_column(Time)

    client: Mapped['Client'] = relationship(back_populates = 'wedding')
    organizator: Mapped['Organizator'] = relationship(back_populates = 'weddings')
    place: Mapped['Place'] = relationship(back_populates = 'weddings')

    def __repr__(self):
        return f'Wedding(partner1_name: {self.partner1_name}, partner2_name: {self.partner2_name}, ' \
               f'date: {self.date}, start_time: {self.start_time}, end_time: {self.end_time}, ' \
               f'client_id: {self.client_id}, organizator_id: {self.organizator_id}, place_id: {self.place_id})'

engine = create_engine('postgresql+psycopg2://postgres:123457896_Qq@localhost:5432/weddings')

class Model:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(
            dbname = "weddings",
            user = "postgres",
            password = "123457896_Qq",
            host = "localhost",
            port = 5432
        )

    def add_client(self, name, phone_number, email) -> None:
        with Session(engine) as session, session.begin():
            session.add(Client(name = name, phone_number = phone_number, email = email))

    def get_all_clients(self):
        with Session(engine) as session:
            return session.scalars(select(Client)).all()
    
    def get_client(self, id):
        with Session(engine) as session:
            return session.get(Client, id)

    def update_client(self, id, name, phone_number, email) -> None:
        with Session(engine) as session:
            update_stmt = update(Client).where(Client.id == id).values(
                name = name,
                phone_number = phone_number,
                email = email
            )
            session.execute(update_stmt)
            session.commit()
    
    def delete_client(self, id):
        with Session(engine) as session:
            delete_stmt = delete(Client).where(Client.id == id)
            session.execute(delete_stmt)
            session.commit()
        

    def add_organizator(self, name, phone_number, email) -> None:
        with Session(engine) as session, session.begin():
            session.add(Organizator(name = name, phone_number = phone_number, email = email))
        
    def get_all_organizators(self):
        with Session(engine) as session:
            return session.scalars(select(Organizator)).all()
        
    def get_organizator(self, id):
        with Session(engine) as session:
            return session.get(Organizator, id)
        
    def update_organizator(self, id, name, phone_number, email) -> None:
        with Session(engine) as session:
            update_stmt = update(Organizator).where(Organizator.id == id).values(
                name = name,
                phone_number = phone_number,
                email = email
            )
            session.execute(update_stmt)
            session.commit()

    def delete_organizator(self, id):
        with Session(engine) as session:
            delete_stmt = delete(Organizator).where(Organizator.id == id)
            session.execute(delete_stmt)
            session.commit()
        

    def add_place(self, name, phone_number, email, address) -> None:
        with Session(engine) as session, session.begin():
            session.add(Place(name = name, phone_number = phone_number, email = email, address = address))

    def get_all_places(self):
        with Session(engine) as session:
            return session.scalars(select(Place)).all()
    
    def get_place(self, id):
        with Session(engine) as session:
            return session.get(Place, id)
        
    def update_place(self, id, name, phone_number, email, address) -> None:
        with Session(engine) as session:
            update_stmt = update(Place).where(Place.id == id).values(
                name = name,
                phone_number = phone_number,
                email = email,
                address = address
            )
            session.execute(update_stmt)
            session.commit()

    def delete_place(self, id):
        with Session(engine) as session:
            delete_stmt = delete(Place).where(Place.id == id)
            session.execute(delete_stmt)
            session.commit()


    def add_wedding(self, partner1_name, partner2_name,
                    date, start_time, end_time,
                    client_id, place_id, organizator_id) -> None:
        with Session(engine) as session, session.begin():
            session.add(Wedding(partner1_name = partner1_name, partner2_name = partner2_name,
                    date = date, start_time = start_time, end_time = end_time,
                    client_id = client_id, place_id = place_id, organizator_id = organizator_id))

    def get_all_weddings(self):
        with Session(engine) as session:
            return session.scalars(select(Wedding)).all()
        
    def get_wedding(self, client_id):
        with Session(engine) as session:
            return session.get(Wedding, client_id)

    def update_wedding(self, partner1_name, partner2_name,
                    date, start_time, end_time,
                    client_id, place_id, organizator_id) -> None:
        with Session(engine) as session:
            update_stmt = update(Wedding).where(Wedding.client_id == client_id).values(
                partner1_name = partner1_name,
                partner2_name = partner2_name,
                date = date,
                start_time = start_time,
                end_time = end_time,
                client_id = client_id,
                place_id = place_id,
                organizator_id = organizator_id
            )   
            session.execute(update_stmt)
            session.commit()

    def delete_wedding(self, client_id):
        with Session(engine) as session:
            delete_stmt = delete(Wedding).where(Wedding.client_id == client_id)
            session.execute(delete_stmt)
            session.commit()


    def generate_batch(self, rows):
        with self.connection.cursor() as cursor:
            try:
                start = time.time_ns()
                cursor.execute(
                    'insert into "Clients" (name, phone_number, email)\n'
                    '(\n'
                    '   select name, \n'
                    "       '+' || rpad((random() * 1000)::int::text, 3, '0') || lpad((random() * 1000000000)::int::text, 9, '0') as phone_number, \n"
                    "       name || '_' || (random() * 1000)::int::varchar(3) || '@' || case when random() > 0.5 then 'gmail.com' else 'ukr.net' end as email\n"
                    '   from (\n'
                    '       select (chr((random() * 25)::int + 65)) || \n'
                    '              (chr((random() * 25)::int + 97)) || \n'
                    '              (chr((random() * 25)::int + 97)) || \n'
                    '              (chr((random() * 25)::int + 97)) as name\n'
                    '       from generate_series(1, %s)\n'
                    '   )\n'
                    ')',
                    [rows])
                cursor.execute(
                    'insert into "Organizators" (name, phone_number, email) \n'
                    '(select	name, \n'
                    "   '+' || rpad((random() * 1000)::int::text, 3, '0') || lpad((random() * 1000000000)::int::text, 9, '0') as phone_number, \n"
                    "   name || '_' || (random() * 1000)::int::varchar(3) || row::text || '@' || case when random() > 0.5 then 'gmail.com' else 'ukr.net' end as email\n"
                    'from	(select (chr((random() * 25)::int + 65)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    '               (chr((random() * 25)::int + 97)) as name, \n'
                    '               row'
                    '        from generate_series(1, %s) as row))',
                    [rows])
                cursor.execute (
                    'insert into "Places" (name, phone_number, email, address) \n'
                    '(select	name, \n'
                    "       '+' || rpad((random() * 1000)::int::text, 3, '0') || lpad((random() * 1000000000)::int::text, 9, '0') as phone_number, \n"
                    "       replace(lower(name), ' ', '_') || '_rest_' || (random() * 1000)::int::varchar(3) || row::text || '@' || case when random() > 0.5 then 'gmail.com' else 'ukr.net' end as email, \n"
                    '       address\n'
                    'from	(select (chr((random() * 25)::int + 65)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    "               (chr((random() * 25)::int + 97)) || ' ' || \n"
                    '               (chr((random() * 25)::int + 65)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    '               (chr((random() * 25)::int + 97)) as name, \n'	
                    "               (random() * 99 + 1)::int::varchar(2) || ' ' || \n"
                    '               (chr((random() * 25)::int + 65)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    '               (chr((random() * 25)::int + 97)) || \n'
                    "               (chr((random() * 25)::int + 97)) || ' St.' as address, \n"
                    '               row'
                    '        from generate_series(1, %s) as row))', 
                    [rows])
                cursor.execute(
                    "with new_weddings as (\n"
                    "select * \n"
                    "from (select	(chr((random() * 25)::int + 65)) || \n"
                    "               (chr((random() * 25)::int + 97)) || \n"
                    "               (chr((random() * 25)::int + 97)) || \n"
                    "               (chr((random() * 25)::int + 97)) as partner1_name, \n"
                    "               (chr((random() * 25)::int + 65)) || \n"
                    "               (chr((random() * 25)::int + 97)) || \n"
                    "               (chr((random() * 25)::int + 97)) || \n"
                    "               (chr((random() * 25)::int + 97)) as partner2_name, \n"
                    "               '2024-01-01'::date + (random() * 365)::int as date, \n"
                    "               make_time((random() * 4 + 12)::int, (random() * 59)::int, 0) as start_time, \n"
                    "               make_time((random() * 5 + 18)::int, (random() * 59)::int, 0) as end_time, \n"
                    "               floor(random() * %s + 1)::int + ((select max(id) from \"Organizators\") - %s) as organizator_id, \n"
                    "               floor(random() * %s + 1)::int + ((select max(id) from \"Places\") - %s) as place_id, \n"
                    "               client_id \n"
                    "               from generate_series((select max(id) - %s + 1 from \"Clients\"), (select max(id) from \"Clients\")) as client_id) \n"
                    ') insert into "Weddings" (partner1_name, partner2_name, date, start_time, end_time, client_id, organizator_id, place_id) '
                    "(select partner1_name, partner2_name, date, start_time, end_time, client_id, organizator_id, place_id from new_weddings)",
                    (rows, rows, rows, rows, rows)
                )
                end = time.time_ns()
            except Exception as e:
                self.connection.rollback()
                raise e
            self.connection.commit()
            return end - start

    
    def client_date_partners(self, left_date, right_date):
        with self.connection.cursor() as cursor:
            start = time.time_ns()
            cursor.execute(
                'select client_id, "Clients".name, date, partner1_name, partner2_name\n'
                'from "Weddings"\n'
                'join "Clients" on client_id = "Clients".id\n'
                "where date >= %s and date <= %s\n"
                'group by client_id, "Clients".name, date, partner1_name, partner2_name\n'
                'order by date asc',
                (left_date, right_date)
            )
            end = time.time_ns()
            return (cursor.fetchall(), end - start)
        
    def organizator_weddings(self, date, min_weddings):
        with self.connection.cursor() as cursor:
            start = time.time_ns()
            cursor.execute(
                'select * \n'
                'from (\n'
                '    select id as organizator, name, phone_number, email, count(client_id) as weddings\n'
                '    from "Weddings"\n'
                '    join "Organizators" on id=organizator_id\n'
                "    where date > %s\n"
                '    group by id, name, phone_number, email\n'
                '    )\n'
                'where weddings >= %s\n'
                'order by weddings desc',
                (date, min_weddings)
            )
            end = time.time_ns()
            return (cursor.fetchall(), end - start)
        
    def weddings_place(self, date):
        with self.connection.cursor() as cursor:
            start = time.time_ns()
            cursor.execute(
                'select count(client_id) as weddings, address, place_id as place\n'
                'from "Clients"\n'
                'join "Weddings" on client_id="Clients".id\n'
                'join "Places" on place_id="Places".id\n'
                'join "Organizators" on organizator_id="Organizators".id\n'
                "where date > %s\n"
                'group by place_id, address\n',
                (date,)
            )
            end = time.time_ns()
            return (cursor.fetchall(), end - start)