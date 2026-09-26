import json
from datetime import date

ATTENDANCE_FILE = "attendance.json"

def load_attendance():
    try:
        with open(ATTENDANCE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_attendance(attendance):
    with open(ATTENDANCE_FILE, "w") as file:
        json.dump(attendance, file, indent=4)

def mark_attendance(roll_no, students):
    if roll_no not in students:
        print("No such student found. Please register first.")
        return

    attendance = load_attendance()
    today = str(date.today())

    if today not in attendance:
        attendance[today] = []

    if roll_no in attendance[today]:
        print(f"{students[roll_no]['name']} is already marked present today.")
        return

    attendance[today].append(roll_no)
    save_attendance(attendance)
    print(f"Attendance marked for {students[roll_no]['name']} (Roll No: {roll_no}) on {today}.")

def view_attendance_for_date():
    attendance = load_attendance()
    check_date = input("Enter date to check (YYYY-MM-DD), or press Enter for today: ").strip()

    if check_date == "":
        check_date = str(date.today())

    if check_date not in attendance or not attendance[check_date]:
        print(f"No attendance records for {check_date}.")
        return

    print(f"\nStudents present on {check_date}:")
    for roll_no in attendance[check_date]:
        print(f"- Roll No: {roll_no}")
        