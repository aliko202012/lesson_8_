import sqlite3

class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

class Student:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect('university.db')
        self.cursor = self.conn.cursor()
        self._create_tables()
        self._add_student()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                credits INTEGER NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS student_courses (
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (course_id) REFERENCES courses(id)
            )
        ''')
        self.conn.commit()

    def _add_student(self):
        self.cursor.execute('INSERT OR IGNORE INTO students (name) VALUES (?)', (self.name,))
        self.conn.commit()

    def add_course(self, course):

        self.cursor.execute('INSERT OR IGNORE INTO courses (name, credits) VALUES (?, ?)',
                            (course.name, course.credits))
        self.conn.commit()
        

        self.cursor.execute('SELECT id FROM students WHERE name = ?', (self.name,))
        student_id = self.cursor.fetchone()[0]
        
        self.cursor.execute('SELECT id FROM courses WHERE name = ?', (course.name,))
        course_id = self.cursor.fetchone()[0]
        

        self.cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)',
                            (student_id, course_id))
        self.conn.commit()

    def total_credits(self):

        self.cursor.execute('''
            SELECT SUM(c.credits) 
            FROM courses c 
            JOIN student_courses sc ON c.id = sc.course_id 
            JOIN students s ON s.id = sc.student_id 
            WHERE s.name = ?
        ''', (self.name,))
        return self.cursor.fetchone()[0] or 0

    def close(self):
        self.conn.close()


course1 = Course("Mathematics", 3)
course2 = Course("Physics", 4)
course3 = Course("Literature", 2)


student1 = Student("Али")
student2 = Student("Кутман")


student1.add_course(course1)
student1.add_course(course2)

student2.add_course(course2)
student2.add_course(course3)


print(f"Общее количество кредитов у {student1.name}: {student1.total_credits()}") 
print(f"Общее количество кредитов у {student2.name}: {student2.total_credits()}")  


student1.close()
student2.close()