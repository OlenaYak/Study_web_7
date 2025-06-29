"""Знайти середній бал, який ставить певний викладач зі своїх предметів."""

from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session


def select_8():
    result = session.query(
        Teacher.fullname.label('teacher_name'),
        Subject.id.label('subject_id'),
        Subject.name.label('subject_name'),
        func.round(func.avg(Grade.grade), 2).label('average_grade_per_subject'),)\
            .join(Subject, Subject.teacher_id == Teacher.id) \
            .join(Grade, Grade.subjects_id == Subject.id) \
            .filter(Teacher.id == 2) \
            .group_by(Teacher.fullname, Subject.id, Subject.name) \
            .order_by(desc('average_grade_per_subject')) \
            .all()
    
    return result


if __name__ == '__main__':
    print(select_8())



# -- по id викладача
# SELECT 
#     t.fullname AS teacher_name,
#     sub.id AS subject_id,
#     sub.name AS subject_name,
#     ROUND(AVG(gr.grade), 2) AS average_grade_per_subject,
#     ROUND(AVG(AVG(gr.grade)) OVER (), 2) AS overall_average_grade
# FROM teachers t
# JOIN subjects sub ON sub.teacher_id = t.id
# JOIN grades gr ON gr.subject_id = sub.id
# WHERE t.id = 2  
# GROUP BY t.fullname, sub.id, sub.name
# ORDER BY average_grade_per_subject DESC;