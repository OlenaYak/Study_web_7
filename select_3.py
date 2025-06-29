"""Знайти середній бал у групах з певного предмета."""

from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session



def select_3():
    result = session.query(Group.id, Group.name.label('group_name'), func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Grade)\
        .join(Student, Grade.student_id == Student.id)\
        .join(Group, Student.group_id == Group.id)\
        .filter(Grade.subjects_id == 1).group_by(Group.id, Group.name).order_by(desc('average_grade')).all()
    return result


if __name__ == '__main__':
    print(select_3())

# SELECT 
#     g.id AS group_id,
#     g.name AS group_name,
#     ROUND(AVG(gr.grade), 2) AS average_grade
# FROM grades gr
# JOIN students s ON gr.student_id = s.id
# JOIN groups g ON s.group_id = g.id
# WHERE gr.subject_id = 1  -- Замінити на потрібний subject_id
# GROUP BY g.id, g.name
# ORDER BY average_grade DESC;