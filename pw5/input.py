from domains.student import Student
from domains.course import Course

def input_students(students):
    n = int(input("Nhập số lượng sinh viên: "))
    for _ in range(n):
        s_id = input("Mã SV: ")
        name = input("Họ tên SV: ")
        dob = input("Ngày sinh (DD/MM/YYYY): ")
        students.append(Student(s_id, name, dob))
    
    # Ghi dữ liệu vào students.txt sau khi nhập xong
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()}\n")
    print("-> Đã lưu sinh viên vào students.txt")

def input_courses(courses):
    n = int(input("Nhập số lượng môn học: "))
    for _ in range(n):
        c_id = input("Mã môn: ")
        name = input("Tên môn: ")
        credits = int(input("Số tín chỉ: "))
        courses.append(Course(c_id, name, credits))
    
    # Ghi dữ liệu vào courses.txt sau khi nhập xong
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")
    print("-> Đã lưu môn học vào courses.txt")

def input_marks(courses, students, marks):
    c_id = input("Nhập mã môn muốn vào điểm: ")
    course_exists = any(c.get_id() == c_id for c in courses)
    if not course_exists:
        print("Mã môn không tồn tại!")
        return

    if c_id not in marks:
        marks[c_id] = {}

    for s in students:
        mark = float(input(f"Nhập điểm cho {s.get_name()} ({s.get_id()}): "))
        marks[c_id][s.get_id()] = mark

    # Ghi toàn bộ bảng điểm vào marks.txt sau khi nhập xong
    with open("marks.txt", "w", encoding="utf-8") as f:
        for course_id, student_marks in marks.items():
            for student_id, mark in student_marks.items():
                f.write(f"{course_id},{student_id},{mark}\n")
    print("-> Đã lưu điểm vào marks.txt")