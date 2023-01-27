from datetime import datetime
import faker
from random import randint
import sqlite3

NUMBER_LECTURERS = 4
NUMBER_STUDENTS = 30
NUMBER_SUBJECTS = 7
GRADE = 10
GROUPS = 3
fake_subjects = ["Chemistry", "Geography", "Geometry", "History", "Literature", "Mathematics", "Biology"]


def generate_fake_data(number_lecturers, number_students) -> tuple():
    fake_lecturers = []
    fake_students = []

    fake_data = faker.Faker()

    for _ in range(number_lecturers):
        fake_lecturers.append(fake_data.name())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    return fake_lecturers, fake_students


def prepare_data(lecturers_data, students_data) -> tuple():
    for_lecturers = []
    for person in lecturers_data:
        for_lecturers.append((person,))

    for_grades = []
    for stu in students_data:
        for grade in range(20):
            grade_date = datetime(2023, randint(1, 12), randint(1, 28)).date()
            for_grades.append((randint(1, NUMBER_STUDENTS), randint(1, NUMBER_SUBJECTS), randint(1, GRADE), grade_date))

    for_groups = []
    for group in range(1, GROUPS + 1):
        for_groups.append((f"group {group}",))

    for_students = []
    for student in students_data:
        for_students.append((student, randint(1, GROUPS)))

    for_subjects = []
    for subject in fake_subjects:
        for_subjects.append((subject, randint(1, NUMBER_LECTURERS)))

    return for_lecturers, for_grades, for_groups, for_students, for_subjects


def insert_data_to_db(lecturers_ins, grades_ins, groups_ins, students_ins, subjects_ins) -> None:

    with sqlite3.connect('students.db') as con:
        cur = con.cursor()

        sql_to_lecturers = """INSERT INTO lecturers(full_name)
                               VALUES (?)"""
        cur.executemany(sql_to_lecturers, lecturers_ins)

        sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, date_stamp)
                               VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades_ins)

        sql_to_st_groups = """INSERT INTO st_groups(group_name)
                                       VALUES (?)"""
        cur.executemany(sql_to_st_groups, groups_ins)

        sql_to_students = """INSERT INTO students(full_name, group_id)
                                       VALUES (?, ?)"""
        cur.executemany(sql_to_students, students_ins)

        sql_to_subjects = """INSERT INTO subjects(subject, lecturer_id)
                                               VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects_ins)

        con.commit()


if __name__ == "__main__":
    lecturers, grades, groups, students, subjects = prepare_data(*generate_fake_data(NUMBER_LECTURERS, NUMBER_STUDENTS))
    insert_data_to_db(lecturers, grades, groups, students, subjects)
