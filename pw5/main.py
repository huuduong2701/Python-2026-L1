import os
import zipfile
from domains.student import Student
from domains.course import Course
import input as inp
import output as outp

DATA_ARCHIVE = "students.dat"
TXT_FILES = ["students.txt", "courses.txt", "marks.txt"]

def load_data(students, courses, marks):
    
    if os.path.exists(DATA_ARCHIVE):
        print(f"Tìm thấy '{DATA_ARCHIVE}', đang tiến hành giải nén...")
        with zipfile.ZipFile(DATA_ARCHIVE, 'r') as archive:
            archive.extractall()
        print("-> Giải nén thành công.")

    
    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    students.append(Student(parts[0], parts[1], parts[2]))

    
    if os.path.exists("courses.txt"):
        with open("courses.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    courses.append(Course(parts[0], parts[1], int(parts[2])))

    
    if os.path.exists("marks.txt"):
        with open("marks.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    c_id, s_id, mark = parts[0], parts[1], float(parts[2])
                    if c_id not in marks:
                        marks[c_id] = {}
                    marks[c_id][s_id] = mark

def compress_data():
    print("\nĐang nén dữ liệu trước khi đóng chương trình...")
    with zipfile.ZipFile(DATA_ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for file in TXT_FILES:
            if os.path.exists(file):
                archive.write(file)
    print(f"-> Đã nén thành công vào file '{DATA_ARCHIVE}'.")

def main():
    students = []
    courses = []
    marks = {}

    
    load_data(students, courses, marks)

    while True:
        print("\n=== QUẢN LÝ ĐIỂM SINH VIÊN (PW5) ===")
        print("1. Nhập thông tin sinh viên")
        print("2. Nhập thông tin môn học")
        print("3. Nhập điểm môn học")
        print("4. Hiển thị danh sách sinh viên")
        print("5. Hiển thị danh sách môn học")
        print("6. Hiển thị điểm")
        print("0. Thoát chương trình")
        
        choice = input("Lựa chọn của bạn: ")

        if choice == "1":
            inp.input_students(students)
        elif choice == "2":
            inp.input_courses(courses)
        elif choice == "3":
            inp.input_marks(courses, students, marks)
        elif choice == "4":
            outp.display_students(students)
        elif choice == "5":
            outp.display_courses(courses)
        elif choice == "6":
            outp.display_marks(marks)
        elif choice == "0":
            
            compress_data()
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()