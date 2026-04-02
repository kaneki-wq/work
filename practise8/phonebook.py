import psycopg2
from connect import get_connection

def call_upsert():
    name = input("Имя: ")
    phone = input("Телефон: ")
    conn = get_connection()
    if conn:
        with conn:
            with conn.cursor() as cur:
                # ВАЖНО: Процедуры вызываются через CALL
                cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        print("Запись обработана (добавлена или обновлена).")
        conn.close()

def call_search():
    pattern = input("Введите часть имени или телефона: ")
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            # Функции, возвращающие таблицы, можно вызывать через callproc
            cur.callproc('get_contacts_by_pattern', (pattern,))
            results = cur.fetchall()
            for r in results:
                print(f"ID: {r[0]} | Name: {r[1]} | Phone: {r[2]}")
        conn.close()

def call_bulk_insert():
    # Пример данных (можно адаптировать под CSV)
    names = ["Valid User", "Bad User"]
    phones = ["123456789", "short"] # "short" не пройдет валидацию в SQL
    
    conn = get_connection()
    if conn:
        with conn:
            with conn.cursor() as cur:
                # Передаем массивы и пустой массив для INOUT параметра
                cur.execute("CALL insert_many_contacts(%s, %s, %s)", (names, phones, []))
                failed = cur.fetchone()[0]
                if failed:
                    print(f"Ошибки валидации в SQL: {failed}")
                else:
                    print("Все записи успешно добавлены.")
        conn.close()

def call_pagination():
    limit = int(input("Записей на странице: "))
    offset = int(input("Пропустить (offset): "))
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.callproc('get_contacts_paginated', (limit, offset))
            for r in cur.fetchall():
                print(f"{r[0]}. {r[1]} - {r[2]}")
        conn.close()

def call_delete():
    target = input("Введите имя или телефон для удаления: ")
    conn = get_connection()
    if conn:
        with conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact(%s)", (target,))
        print("Команда удаления выполнена.")
        conn.close()

def menu():
    while True:
        print("\n--- PhoneBook Practice 8 (Procedures) ---")
        print("1. Добавить/Обновить (Upsert)")
        print("2. Поиск по паттерну (Function)")
        print("3. Массовая вставка (Bulk + Validation)")
        print("4. Показать с пагинацией")
        print("5. Удалить")
        print("6. Выход")
        
        choice = input("Выбор: ")
        if choice == '1': call_upsert()
        elif choice == '2': call_search()
        elif choice == '3': call_bulk_insert()
        elif choice == '4': call_pagination()
        elif choice == '5': call_delete()
        elif choice == '6': break

if __name__ == "__main__":
    menu()