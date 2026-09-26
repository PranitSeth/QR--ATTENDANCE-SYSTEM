import json
from qr_generator import generate_qr_for_student, generate_qr_for_all
from attendance import mark_attendance, view_attendance_for_date
from reports import view_all_students, show_attendance_summary, show_top_attendance, show_kth_highest_attendance

FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def register_student(students):
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    if roll_no in students:
        print("Student already exists.")
        return

    students[roll_no] = {
        "name": name,
        "phone": phone
    }

    save_students(students)
    print("Student registered successfully!")

def main():
    students = load_students()

    while True:
        print("\n===== QR ATTENDANCE SYSTEM =====")
        print("1. Register Student")
        print("2. Generate QR Code for a Student")
        print("3. Generate QR Codes for All Students")
        print("4. Mark Attendance")
        print("5. View Attendance for a Date")
        print("6. View All Students")
        print("7. Attendance Summary (all students)")
        print("8. Top N Students by Attendance")
        print("9. Find Kth Highest Attendance")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_student(students)
        elif choice == "2":
            roll_no = input("Enter Roll Number: ")
            generate_qr_for_student(roll_no, students)
        elif choice == "3":
            generate_qr_for_all(students)
        elif choice == "4":
            roll_no = input("Enter Roll Number: ")
            mark_attendance(roll_no, students)
        elif choice == "5":
            view_attendance_for_date()
        elif choice == "6":
            view_all_students(students)
        elif choice == "7":
            show_attendance_summary(students)
        elif choice == "8":
            n = int(input("Enter N: "))
            show_top_attendance(students, n)
        elif choice == "9":
            k = int(input("Enter K: "))
            show_kth_highest_attendance(students, k)
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
