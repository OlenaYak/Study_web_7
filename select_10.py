"""Список курсів, які певному студенту читає певний викладач."""

from sqlalchemy import func, desc, select, and_, distinct

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session



def select_10():
    result = session.query(
        Student.fullname.label('student_name'),
        Teacher.fullname.label('teacher_name'),
        Subject.id.label('subject_id'),
        Subject.name.label('subject_name'))\
          .select_from(Grade)\
          .join(Student, Grade.student_id == Student.id) \
          .join(Subject, Grade.subjects_id == Subject.id) \
          .join(Teacher, Subject.teacher_id == Teacher.id) \
          .filter(Student.id == 3, Teacher.id == 1) \
          .order_by(Subject.name).distinct().all()
          
    return result

if __name__ == '__main__':
    print(select_10())



# SELECT DISTINCT
#     s.fullname AS student_name,
#     t.fullname AS teacher_name,
#     sub.id AS subject_id,
#     sub.name AS subject_name
# FROM grades gr
# JOIN students s ON gr.student_id = s.id
# JOIN subjects sub ON gr.subject_id = sub.id
# JOIN teachers t ON sub.teacher_id = t.id
# WHERE s.id = 3  
#   AND t.id = 1   
# ORDER BY sub.name;
