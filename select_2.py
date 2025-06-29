"""Знайти студента із найвищим середнім балом з певного предмета."""

from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session

def select_2():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Grade). join(Student).filter(Grade.subjects_id==1).group_by(Student.id). order_by(desc('average_grade')).limit(1).all()
    return result


if __name__ == '__main__':
    print(select_2())





# SELECT 
#     s.id,
#     s.fullname,
#     sub.name AS subject_name,
#     ROUND(AVG(g.grade)) AS average_grade
# FROM students s
# JOIN grades g ON s.id = g.student_id
# JOIN subjects sub ON g.subject_id = sub.id
# WHERE g.subject_id = 1
# GROUP BY s.id, s.fullname, sub.name
# ORDER BY average_grade DESC
# LIMIT 1;
