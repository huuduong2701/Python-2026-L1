import os
import pickle
import gzip
import input as inp
import output as outp

DATA_FILE = "students.dat"

def load_data():
    """Load pickled and compressed data from students.dat."""
    if os.path.exists(DATA_FILE):
        print(f"Found '{DATA_FILE}', loading data...")
        try:
            with gzip.open(DATA_FILE, "rb") as f:
                data = pickle.load(f)
                print("-> Data loaded successfully.")
                return data.get("students", []), data.get("courses", []), data.get("marks", {})
        except Exception as e:
            print(f"Error loading '{DATA_FILE}': {e}")
    return [], [], {}

def save_data(students, courses, marks):
    """Serialize and compress data into students.dat using pickle."""
    print("\nSaving and compressing data...")
    data = {
        "students": students,
        "courses": courses,
        "marks": marks
    }
    with gzip.open(DATA_FILE, "wb") as f:
        pickle.dump(data, f)
    print(f"-> Successfully saved into '{DATA_FILE}'.")

def main():
    students, courses, marks = load_data()

    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM (PW6 - PICKLE) ===")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Display Students")
        print("5. Display Courses")
        print("6. Display Marks")
        print("0. Save and Exit")

        choice = input("Enter choice: ").strip()

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
            save_data(students, courses, marks)
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()