import psycopg2
import csv

# 1. Настройки подключения
params = {
    "host": "127.0.0.1",
    "database": "postgres",
    "user": "postgres",
    "password": "пароль"  
}

def get_connection():
    # Создаем подключение и сразу ставим кодировку UTF8
    conn = psycopg2.connect(**params)
    conn.set_client_encoding('UTF8')
    return conn

# --- 2. Вставка данных из консоли ---
def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print(f"Контакт {name} успешно добавлен!")
    except Exception as e:
        print(f"Ошибка при добавлении: {e}")
    finally:
        cur.close()
        conn.close()

# --- 3. Загрузка из CSV файла ---
def upload_from_csv(file_path):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # Указываем encoding='utf-8', чтобы не было ошибок чтения
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Пропускаем заголовок (first_name, phone)
            for row in reader:
                # Используем ON CONFLICT, чтобы не было ошибок, если номер уже есть
                cur.execute("""
                    INSERT INTO phonebook (first_name, phone) 
                    VALUES (%s, %s) 
                    ON CONFLICT (phone) DO NOTHING
                """, row)
        conn.commit()
        print("Данные из CSV успешно загружены!")
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
    finally:
        cur.close()
        conn.close()

# --- 4. Обновление данных ---
def update_contact(name, new_phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()
    print(f"Контакт {name} обновлен.")
    cur.close()
    conn.close()

# --- 5. Поиск данных (Фильтры) ---
def query_contacts(name_filter="%"):
    conn = get_connection()
    cur = conn.cursor()
    # Фильтр по части имени (например, 'Iv%' найдет Ivan)
    cur.execute("SELECT id, first_name, phone FROM phonebook WHERE first_name LIKE %s", (name_filter,))
    rows = cur.fetchall()
    print("\n--- Список контактов ---")
    for row in rows:
        print(f"ID: {row[0]} | Имя: {row[1]} | Тел: {row[2]}")
    cur.close()
    conn.close()

# --- 6. Удаление по имени или телефону ---
def delete_contact(identifier):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE first_name = %s OR phone = %s", (identifier, identifier))
    conn.commit()
    print(f"Контакт(ы) с идентификатором '{identifier}' удален(ы).")
    cur.close()
    conn.close()

# --- ГЛАВНЫЙ БЛОК ЗАПУСКА ---
if __name__ == "__main__":
    # Вызываем функции по очереди для теста:
    
    print("1. Пробуем загрузить данные из data.csv...")
    upload_from_csv('data.csv')
    
    print("\n2. Текущий список в базе:")
    query_contacts()
    
    print("\n3. Обновим телефон для 'Ivan' (если он есть):")
    update_contact('Ivan', '87770000000')
    
    print("\n4. Список после обновления:")
    query_contacts()
    
    # print("\n5. Теперь можешь ввести данные вручную:")
    # insert_from_console()