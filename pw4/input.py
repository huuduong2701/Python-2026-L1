import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import math
from domains.student import Student
from domains.course import Course


def round_down_1_dec(val):
    return math.floor(val * 10) / 10

def input_courses():
    courses = []
    num_c = int(input("Nhập số lượng khóa học: "))
    for _ in range(num_c):
        c_id = input("Mã khóa học: ")
        name = input("Tên khóa học: ")
        credits = int(input("Số tín chỉ: "))
        courses.append(Course(c_id, name, credits))
    return courses

def input_students():
    students = []
    num_s = int(input("Nhập số lượng sinh viên: "))
    for _ in range(num_s):
        s_id = input("Mã sinh viên: ")
        name = input("Tên sinh viên: ")
        dob = input("Ngày sinh: ")
        students.append(Student(s_id, name, dob))
    return students

def input_marks(students, courses):
    for c in courses:
        print(f"\n--- Nhập điểm cho môn {c.name} ({c.id}) ---")
        for s in students:
            score = float(input(f"Điểm của SV {s.name} ({s.id}): "))
            s.marks[c.id] = round_down_1_dec(score)