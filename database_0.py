import sqlite3

db = sqlite3.connect('vedomosti14.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS students (
   ФИО TEXT,
   оценка TEXT
)""")

db.commit()

student_ФИО = input('ФИО: ')

sql.execute(f"SELECT ФИО FROM students WHERE ФИО = (?)", (student_ФИО))
if sql.fetchone() is None:
    student_оценка = input('оценка: ')
    sql.execute(f"INSERT INTO students VALUES (?, ?)", (student_ФИО, student_оценка))
    db.commit()
    
    print('Вы заполнили ведомости')
else:
    print("Вы уже заполняли ведомости")
    for value in sql.execute("SELECT * FROM students"):
        print(value)

                  
