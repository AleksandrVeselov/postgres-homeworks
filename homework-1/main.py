"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


def open_csv_file(csv_file: str) -> dict:
    """
    Функция для чтения CSV файла
    """
    with open(csv_file, 'r', encoding='UTF-8') as read_file:
        data = csv.DictReader(read_file)
        for d in data:
            yield d


# параметры для подключения к базе данных
params = {'host': 'localhost', 'database': 'north', 'user': 'postgres', 'password': '12356'}

with psycopg2.connect(**params) as conn:
    with conn.cursor() as cur:

        # заполнение данными таблицы employees_data
        employees = open_csv_file('../homework-1/north_data/employees_data.csv')

        for employee in employees:
            cur.execute('INSERT INTO employees_data (first_name, last_name, title, birth_date, notes)'
                        ' VALUES (%s, %s, %s, %s, %s)',
                        (employee['first_name'], employee['last_name'], employee['title'],
                         employee['birth_date'], employee['notes']))

        # заполнение данными таблицы customers_data
        customers = open_csv_file('../homework-1/north_data/customers_data.csv')
        for customer in customers:
            cur.execute('INSERT INTO customers_data VALUES (%s, %s, %s)', (customer['customer_id'],
                                                                           customer['company_name'],
                                                                           customer['contact_name']))

        # заполнение данными таблицы orders_data
        orders = open_csv_file('../homework-1/north_data/orders_data.csv')
        for order in orders:
            cur.execute('INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)', (order['order_id'],
                                                                                order['customer_id'],
                                                                                order['employee_id'],
                                                                                order['order_date'],
                                                                                order['ship_city']))
