"""Знайти середній бал на потоці (по всій таблиці оцінок)."""

from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session



def select_4():
    result = session.query(
        func.round(func.avg(Grade.grade), 2).label('average_grade_overall')
    ).one()
    
    return result



if __name__ == '__main__':
    print(select_4())


# SELECT 
#     ROUND(AVG(grade), 2) AS average_grade_overall
# FROM grades;