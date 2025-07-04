"""Знайти 5 студентів із найбільшим середнім балом з усіх предметів. """

from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session



def select_1():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Student). join(Grade).group_by(Student.id). order_by(desc('average_grade')).limit(5).all()
    return result


if __name__ == '__main__':
    print(select_1())



# SELECT
#     s.id,
#     s.fullname,
#     ROUND(AVG(g.grade), 2) AS average_grade
# FROM students s
# JOIN grades g ON s.id = g.student_id
# GROUP BY s.id
# ORDER BY average_grade DESC
# LIMIT 5;