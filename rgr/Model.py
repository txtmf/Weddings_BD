import time
import psycopg2

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
        with self.connection.cursor() as cursor:
            cursor.execute('INSERT INTO public."Clients" (name, phone_number, email) VALUES (%s, %s, %s)', (name, phone_number, email))
            self.connection.commit()

    def get_all_clients(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM public."Clients"')
            return cursor.fetchall()
    
    def get_client(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM public."Clients" WHERE id=%s', [id])
            return cursor.fetchall()

    def update_client(self, id, name, phone_number, email) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute('UPDATE public."Clients" SET name=%s, phone_number=%s, email=%s  WHERE id=%s', (name, phone_number, email, id))
            self.connection.commit()
    
    def delete_client(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute('DELETE FROM public."Clients" WHERE id=%s', [id])
            self.connection.commit()
        

    def add_organizator(self, name, phone_number, email) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute('INSERT INTO public."Organizators" (name, phone_number, email) VALUES (%s, %s, %s)', (name, phone_number, email))
            self.connection.commit()
    
    def get_all_organizators(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM public."Organizators"')
            return cursor.fetchall()
        
    def get_organizator(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM public."Organizators" WHERE id=%s', [id])
            return cursor.fetchall()
        
    def update_organizator(self, id, name, phone_number, email) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute('UPDATE public."Organizators" SET name=%s, phone_number=%s, email=%s  WHERE id=%s', (name, phone_number, email, id))
            self.connection.commit()

    def delete_organizator(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute('DELETE FROM public."Organizators" WHERE id=%s', [id])
            self.connection.commit()
        

    def add_place(self, name, phone_number, email, address) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute('INSERT INTO public."Places" (name, phone_number, email, address) VALUES (%s, %s, %s, %s)', (name, phone_number, email, address))
            self.connection.commit()

    def get_all_places(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM public."Places"')
            return cursor.fetchall()
    
    def get_place(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM public."Places" WHERE id=%s', [id])
            return cursor.fetchall()
        
    def update_place(self, id, name, phone_number, email, address) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute('UPDATE public."Places" SET name=%s, phone_number=%s, email=%s, address=%s  WHERE id=%s', (name, phone_number, email, address, id))
            self.connection.commit()

    def delete_place(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute('DELETE FROM public."Places" WHERE id=%s', [id])
            self.connection.commit()


    def add_wedding(self, partner1_name, partner2_name,
                    date, start_time, end_time,
                    client_id, place_id, organizator_id) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute('INSERT INTO public."Weddings" (partner1_name, partner2_name, '
                           'date, start_time, end_time, '
                           'client_id, place_id, organizator_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                           (partner1_name, partner2_name,
                            date, start_time, end_time,
                            client_id, place_id, organizator_id))
            self.connection.commit()

    def get_all_weddings(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM public."Weddings"')
            return cursor.fetchall()
        
    def get_wedding(self, client_id):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM public."Weddings" WHERE client_id=%s', [client_id])
            return cursor.fetchall()
        
    def update_organizator(self, id, name, phone_number, email) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute('UPDATE public."Organizators" SET name=%s, phone_number=%s, email=%s  WHERE id=%s', (name, phone_number, email, id))
            self.connection.commit()

    def update_wedding(self, partner1_name, partner2_name,
                    date, start_time, end_time,
                    client_id, place_id, organizator_id) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute('UPDATE public."Weddings" SET partner1_name=%s, partner2_name=%s, '
                           'date=%s, start_time=%s, end_time=%s, '
                           'place_id=%s, organizator_id=%s WHERE client_id=%s', 
                           (partner1_name, partner2_name,
                            date, start_time, end_time,
                            place_id, organizator_id, client_id))
            self.connection.commit()

    def delete_wedding(self, client_id):
        with self.connection.cursor() as cursor:
            cursor.execute('DELETE FROM public."Weddings" WHERE client_id=%s', [client_id])
            self.connection.commit()


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