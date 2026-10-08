def display_students(students):
    print("\n--- DANH SÁCH SINH VIÊN ---")
    for s in students:
        print(f"ID: {s.get_id()} | Tên: {s.get_name()} | DoB: {s.get_dob()}")

def display_courses(courses):
    print("\n--- DANH SÁCH MÔN HỌC ---")
    for c in courses:
        print(f"ID: {c.get_id()} | Tên: {c.get_name()} | Tín chỉ: {c.get_credits()}")

def display_marks(marks):
    print("\n--- BẢNG ĐIỂM ---")
    for c_id, student_marks in marks.items():
        print(f"Môn {c_id}:")
        for s_id, mark in student_marks.items():
            print(f"  SV {s_id}: {mark}")