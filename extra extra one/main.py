import os
import pickle
import gzip
import csv
import pandas as pd

DATA_FILE = "students.dat"

class Student:
    def __init__(self, s_id, name, dob):
        self.id = s_id
        self.name = name
        self.dob = dob

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

class Course:
    def __init__(self, c_id, name, credits):
        self.id = c_id
        self.name = name
        self.credits = credits

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_credits(self):
        return self.credits

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with gzip.open(DATA_FILE, "rb") as f:
                data = pickle.load(f)
                return data.get("students", []), data.get("courses", []), data.get("marks", {})
        except Exception as e:
            print(f"Error loading '{DATA_FILE}': {e}")
    return [], [], {}

def save_data(students, courses, marks):
    data = {
        "students": students,
        "courses": courses,
        "marks": marks
    }
    with gzip.open(DATA_FILE, "wb") as f:
        pickle.dump(data, f)
    print("Data saved successfully.")

def input_students(students):
    num = int(input("Enter number of students: "))
    for _ in range(num):
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth (DD/MM/YYYY): ")
        students.append(Student(s_id, name, dob))

def input_courses(courses):
    num = int(input("Enter number of courses: "))
    for _ in range(num):
        c_id = input("Course ID: ")
        name = input("Course Name: ")
        credits = int(input("Credits: "))
        courses.append(Course(c_id, name, credits))

def input_marks(courses, students, marks):
    c_id = input("Enter Course ID: ")
    if not any(c.get_id() == c_id for c in courses):
        print("Course ID does not exist!")
        return
    if c_id not in marks:
        marks[c_id] = {}
    for s in students:
        mark = float(input(f"Enter mark for {s.get_name()} ({s.get_id()}): "))
        marks[c_id][s.get_id()] = mark

def display_students(students):
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s.get_id()} | Name: {s.get_name()} | DoB: {s.get_dob()}")

def display_courses(courses):
    print("\n--- Course List ---")
    for c in courses:
        print(f"ID: {c.get_id()} | Name: {c.get_name()} | Credits: {c.get_credits()}")

def display_marks(marks):
    print("\n--- Marks ---")
    for c_id, s_marks in marks.items():
        print(f"Course: {c_id}")
        for s_id, mark in s_marks.items():
            print(f"  Student {s_id}: {mark}")

def export_to_csv(students, courses, marks):
    with open("students.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "dob"])
        for s in students:
            writer.writerow([s.get_id(), s.get_name(), s.get_dob()])

    with open("courses.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "credits"])
        for c in courses:
            writer.writerow([c.get_id(), c.get_name(), c.get_credits()])

    with open("marks.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["course_id", "student_id", "mark"])
        for course_id, student_marks in marks.items():
            for student_id, mark in student_marks.items():
                writer.writerow([course_id, student_id, mark])

    print("Data successfully exported to CSV files.")

def query_students():
    try:
        df_students = pd.read_csv("students.csv")
        print("\n--- Students DataFrame ---")
        print(df_students)

        condition = input("\nEnter query condition (e.g. name == 'Mr. Happy'): ").strip()
        result = df_students.query(condition)

        print("\n--- Query Result ---")
        if result.empty:
            print("No matching records found.")
        else:
            print(result)
    except FileNotFoundError:
        print("Error: students.csv not found. Please export data first.")
    except Exception as e:
        print(f"Query error: {e}")

def main():
    students, courses, marks = load_data()

    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Display Students")
        print("5. Display Courses")
        print("6. Display Marks")
        print("7. Export to CSV")
        print("8. Query Students with Pandas")
        print("0. Save and Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            input_students(students)
        elif choice == "2":
            input_courses(courses)
        elif choice == "3":
            input_marks(courses, students, marks)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            display_courses(courses)
        elif choice == "6":
            display_marks(marks)
        elif choice == "7":
            export_to_csv(students, courses, marks)
        elif choice == "8":
            query_students()
        elif choice == "0":
            save_data(students, courses, marks)
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()