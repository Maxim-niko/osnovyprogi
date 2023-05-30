import sqlite3

db = sqlite3.connect("Vedomosti.db")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS students (
   ФИО TEXT,
   оценка NUMBER
)""")

db.commit()

if input("Вход или регистрация? 1 \ 2: ") == "1":
    ФИО = input("ФИО: ")
                  
    sql.execute(f"SELECT ФИО FROM students WHERE ФИО = '{ФИО}'")
    if not sql.fetchone() is None:
                  оценка = input("оценка: ")
                  
                  sql.execute(f"SELECT ФИО, оценка FROM students WHERE ФИО = '{ФИО}'")

                  if sql.fetchone()[1] == оценка:
                      print("Вы уже заполняли ведомости")
                  else:
                      print("А всё надо было раньше")
           
    else:
        print("Студент был отчислен")
                  
else:
    student_ФИО = input('ФИО: ')
    student_оценка = input('оценка: ')

    sql.execute(f"SELECT ФИО FROM students WHERE ФИО = '{student_ФИО}'")
    if sql.fetchone() is None:
       sql.execute("INSERT INTO students VALUES (?, ?)", (student_ФИО, student_оценка))
       db.commit() 
    else:
        print("Вы заполнили ведомости")
if student_оценка == 3:
    print('Вы слетели со стипы')
if student_оценка == 2:
    print('На допсу')
else:
    print('Так держать')
