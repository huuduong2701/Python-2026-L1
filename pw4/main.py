import sys
import os
import curses
import input as ui_in
import output as ui_out

def main():
    courses = ui_in.input_courses()
    students = ui_in.input_students()
    ui_in.input_marks(students, courses)

    # Tính điểm GPA cho toàn bộ sinh viên
    for s in students:
        s.calculate_gpa(courses)

    # Sắp xếp giảm dần theo GPA
    students.sort(key=lambda s: s.gpa, reverse=True)

    # Hiển thị UI Curses
    curses.wrapper(ui_out.display_curses, students, courses)

if __name__ == "__main__":
    main()