"""Знайти список студентів у певній групі."""

from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session

def select_6():
    result = session.query(Student.id.label('student_id'),Student.fullname.label('student_name'),Group.name.label('group_name'))\
        .join(Group, Student.group_id == Group.id).filter(Student.group_id == 1).order_by(Student.fullname).all()
    
    return result


if __name__ == '__main__':
    print(select_6())


# -- по group_id

# SELECT 
#     s.id AS student_id,
#     s.fullname AS student_name,
#     g.name AS group_name
# FROM students s
# JOIN groups g ON s.group_id = g.id
# WHERE s.group_id = 1
# ORDER BY s.fullname;