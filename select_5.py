"""Знайти які курси читає певний викладач."""

from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session

def select_5():
    result = session.query(Teacher.fullname.label('teacher_name'),Subject.id.label('subject_id'),Subject.name.label('subject_name'))\
        .join(Teacher, Subject.teacher_id == Teacher.id).filter(Teacher.id == 2).all()
    
    return result


if __name__ == '__main__':
    print(select_5())


# -- пошук по id викладача

# SELECT 
#     t.fullname AS teacher_name,
#     sub.id AS subject_id,
#     sub.name AS subject_name
# FROM subjects sub
# JOIN teachers t ON sub.teacher_id = t.id
# WHERE t.id = 2; 