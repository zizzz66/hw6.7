import sqlite3

# Создаем подключение к базе данных (или создаем новую, если она не существует)
conn = sqlite3.connect('students.db')

# Создаем курсор для выполнения операций с базой данных
cursor = conn.cursor()

# Создаем таблицу "students" с указанными полями
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hobby TEXT,
        first_name TEXT,
        last_name TEXT,
        birth_year INTEGER,
        homework_score INTEGER
    )
''')

# Создаем список студентов
students = [
    ('Футбол', 'Иван', 'Петрович', 1998, 15),
    ('Хоккей', 'Анна', 'Сидорова', 1999, 8),
    ('Плавание', 'Дмитрий', 'Иванович', 2000, 12),
    ('Теннис', 'Екатерина', 'Смирнова', 1997, 20),
    ('Баскетбол', 'Алексей', 'Попов', 2001, 5),
    ('Волейбол', 'Мария', 'Федорова', 1999, 14),
    ('Шахматы', 'Андрей', 'Михайлович', 1998, 18),
    ('Фотография', 'Ольга', 'Васильева', 2000, 11),
    ('Кино', 'Артем', 'Николаев', 2002, 9),
    ('Музыка', 'Анастасия', 'Козлова', 1997, 16)
]

# Вставляем студентов в таблицу
cursor.executemany('INSERT INTO students (hobby, first_name, last_name, birth_year, homework_score) VALUES (?,?,?,?,?)', students)

# Сохраняем изменения
conn.commit()

# Достаем всех студентов с фамилией длиннее 10 символов
cursor.execute('SELECT * FROM students WHERE LENGTH(last_name) > 10')
results = cursor.fetchall()
print("Студенты с фамилией длиннее 10 символов:")
for row in results:
    print(row)

# Изменяем имена всех студентов, у которых баллы за ДЗ больше 10, на "genius"
cursor.execute('UPDATE students SET first_name = "genius" WHERE homework_score > 10')

# Сохраняем изменения
conn.commit()

# Достаем всех "genius"
cursor.execute('SELECT * FROM students WHERE first_name = "genius"')
results = cursor.fetchall()
print("Студенты с именем 'genius':")
for row in results:
    print(row)

# Удаляем всех студентов с четным ID
cursor.execute('DELETE FROM students WHERE id % 2 = 0')

# Сохраняем изменения