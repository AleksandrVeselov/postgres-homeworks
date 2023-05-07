import json

import psycopg2

from config import config


def main():
    script_file = 'fill_db.sql'
    json_file = 'suppliers.json'
    db_name = 'my_new_db'

    params = config()
    conn = None

    create_database(params, db_name)
    print(f"БД {db_name} успешно создана")

    params.update({'dbname': db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                execute_sql_script(cur, script_file)
                print(f"БД {db_name} успешно заполнена")

                create_suppliers_table(cur)
                print("Таблица suppliers успешно создана")

                suppliers = get_suppliers_data(json_file)
                insert_suppliers_data(cur, suppliers)
                print("Данные в suppliers успешно добавлены")

                add_foreign_keys(cur, json_file)
                print(f"FOREIGN KEY успешно добавлены")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def create_database(params, db_name) -> None:
    """Создает новую базу данных."""
    conn = psycopg2.connect(**params)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        cur.execute(f'DROP DATABASE {db_name}')  # Пробуем удалить базу данных
    except psycopg2.errors.InvalidCatalogName:
        pass  # Перехватываем ошибку если базы данных с таким именем не существует

    cur.execute(f'CREATE DATABASE {db_name}')  # Создание базы данных

    cur.close()
    conn.close()


def execute_sql_script(cur, script_file) -> None:
    """Выполняет скрипт из файла для заполнения БД данными."""

    with open(script_file, 'r', encoding='UTF-8') as execute_sql_file:
        sql_script = execute_sql_file.read()
        cur.execute(sql_script)


def create_suppliers_table(cur) -> None:
    """Создает таблицу suppliers"""
    cur.execute('CREATE TABLE suppliers ('
                'supplier_id serial primary key, '
                'company_name varchar(50), '
                'contact varchar(50), '
                'address varchar(50), '
                'phone varchar(50), '
                'fax varchar(50), '
                'homepage varchar(50), '
                'products varchar(50))')



def get_suppliers_data(json_file: str) -> list[dict]:
    """Извлекает данные о поставщиках из JSON-файла и возвращает список словарей с соответствующей информацией."""
    pass


def insert_suppliers_data(cur, suppliers: list[dict]) -> None:
    """Добавляет данные из suppliers в таблицу suppliers."""
    pass


def add_foreign_keys(cur, json_file) -> None:
    """Добавляет foreign key со ссылкой на supplier_id в таблицу products."""
    pass


if __name__ == '__main__':
    db_name = 'my_new_db'
    params = config()
    script_file = 'fill_db.sql'
    conn = None
    create_database(params, db_name)
    params.update({'dbname': db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                execute_sql_script(cur, script_file)
                print(f"БД {db_name} успешно заполнена")
                create_suppliers_table(cur)
                print("Таблица suppliers успешно создана")
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
    # main()
