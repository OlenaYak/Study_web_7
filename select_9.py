"""Знайти список курсів, які відвідує студент."""

from sqlalchemy import func, desc, select, and_, distinct

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session


def select_9():
    result = session.query(
        Student.fullname.label('student_name'),
        Subject.id.label('subject_id'),
        Subject.name.label('subject_name')).select_from(Grade)\
            .join(Subject, Grade.subjects_id == Subject.id) \
            .join(Student, Grade.student_id == Student.id) \
            .filter(Student.id == 5) \
            .order_by(Subject.name).distinct().all()
    
    return result

if __name__ == '__main__':
    print(select_9())

# SELECT DISTINCT
#     s.fullname AS student_name,
#     sub.id AS subject_id,
#     sub.name AS subject_name
# FROM grades gr
# JOIN subjects sub ON gr.subject_id = sub.id
# JOIN students s ON gr.student_id = s.id
# WHERE s.id = 5
# ORDER BY sub.name;