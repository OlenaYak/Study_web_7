from faker import Faker
import random
from sqlalchemy import text

from conf.db import session  
from conf.models import Student, Group, Teacher, Subject, Grade 

fake = Faker()

def seed():
    # Очищуємо таблиці та скидаємо sequence (id) через TRUNCATE
    session.execute(text("TRUNCATE TABLE grades RESTART IDENTITY CASCADE;"))
    session.execute(text("TRUNCATE TABLE students RESTART IDENTITY CASCADE;"))
    session.execute(text("TRUNCATE TABLE subjects RESTART IDENTITY CASCADE;"))
    session.execute(text("TRUNCATE TABLE teachers RESTART IDENTITY CASCADE;"))
    session.execute(text("TRUNCATE TABLE groups RESTART IDENTITY CASCADE;"))
    session.commit()

    # Створюємо групи
    groups = [Group(name=f'Group {i}') for i in range(1, 4)]
    session.add_all(groups)
    session.commit()

    # Створюємо викладачів
    teachers = [Teacher(fullname=fake.name()) for _ in range(4)]
    session.add_all(teachers)
    session.commit()

    # Створюємо предмети
    subjects = []
    for _ in range(6):
        subject = Subject(
            name=fake.word().capitalize(),
            teacher=random.choice(teachers)
        )
        subjects.append(subject)
    session.add_all(subjects)
    session.commit()

    # Створюємо студентів
    students = []
    for _ in range(40):
        student = Student(
            fullname=fake.name(),
            group=random.choice(groups)
        )
        students.append(student)
    session.add_all(students)
    session.commit()

    # Додаємо оцінки студентам
    for student in students:
        grades_count = random.randint(10, 20)
        for _ in range(grades_count):
            grade = Grade(
                grade=random.randint(30, 100),
                grade_date=fake.date_between(start_date='-1y', end_date='today'),
                student=student,
                discipline=random.choice(subjects)
            )
            session.add(grade)

    session.commit()
    print("Seeding complete!")

if __name__ == '__main__':
    seed()
