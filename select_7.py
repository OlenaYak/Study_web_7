"""Знайти оцінки студентів у окремій групі з певного предмета."""

from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session

def select_7():
    result = session.query(Student.id.label('student_id'),
        Student.fullname.label('student_name'),
        Group.name.label('group_name'),
        Subject.name.label('subject_name'),
        Grade.grade,
        Grade.grade_date)\
          .join(Student, Grade.student_id == Student.id) \
          .join(Group, Student.group_id == Group.id) \
          .join(Subject, Grade.subjects_id == Subject.id) \
          .filter(Student.group_id == 1, Grade.subjects_id == 2) \
          .order_by(Student.fullname, Grade.grade_date) \
          .all()
    return result

if __name__ == '__main__':
    print(select_7())

# SELECT 
#     s.id AS student_id,
#     s.fullname AS student_name,
#     g.name AS group_name,
#     sub.name AS subject_name,
#     gr.grade,
#     gr.grade_date
# FROM grades gr
# JOIN students s ON gr.student_id = s.id
# JOIN groups g ON s.group_id = g.id
# JOIN subjects sub ON gr.subject_id = sub.id
# WHERE s.group_id = 1
#   AND gr.subject_id = 2
# ORDER BY s.fullname, gr.grade_date;