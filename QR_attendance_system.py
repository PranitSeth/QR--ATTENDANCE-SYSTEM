from excel_store import add_student
from qr_session import start_class_session
from reports import view_all_students, show_attendance_summary, show_top_attendance
from excel_store import add_student, delete_student

def main():
    while True:
        print("\n===== QR ATTENDANCE SYSTEM =====")
        print("1. Register Student")
        print("2. Start Class Session")
        print("3. View All Students")
        print("4. Attendance Summary")
        print("5. Top N Students by Attendance")
        print("6. Delete Student")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll_no = input("Enter Reg No: ")
            name = input("Enter Name: ")
            if add_student(roll_no, name):
                print("Student registered successfully!")
            else:
                print("Student already exists.")
        elif choice == "2":
            label = input("Enter class label (e.g. CSE 3:00 2026-09-29): ")
            start_class_session(label)
        elif choice == "3":
            view_all_students()
        elif choice == "4":
            show_attendance_summary()
        elif choice == "5":
            n = int(input("Enter N: "))
            show_top_attendance(n)
        elif choice == "6":
            reg_no = input("Enter Reg No to delete: ")
            if delete_student(reg_no):
                print("Student deleted.")
            else:
                print("Student not found.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            break
    else:
        print("Invalid choice!")
 
if __name__ == "__main__":
    main()