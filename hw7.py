
import sqlite3

# Функция для удаления студента по его ID
def delete_student_by_id(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()

# Функция для изменения всех полей студента по его ID
def update_student_by_id(student_id, hobby, first_name, last_name, birth_year, homework_score):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET hobby = ?, first_name = ?, last_name = ?, birth_year = ?, homework_score = ?
        WHERE id = ?
    ''', (hobby, first_name, last_name, birth_year, homework_score, student_id))
    conn.commit()
    conn.close()

# Функция для вывода всех студентов
def print_all_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.close()

# Пример использования функций
delete_student_by_id(2)  # Удалить студента с ID 2

update_student_by_id(1, 'Футбол', 'John', 'Doe', 1998, 20)  # Изменить данные студента с ID 1

print_all_students()  # Вывести все данные студентов после изменений