import json
from attendance import load_attendance

FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def view_all_students(students):
    if not students:
        print("No students registered yet.")
        return

    print("\n--- All Registered Students ---")
    for roll_no, info in students.items():
        print(f"Roll No: {roll_no} | Name: {info['name']} | Phone: {info['phone']}")

def attendance_count_per_student(students):
    attendance = load_attendance()
    counts = {roll_no: 0 for roll_no in students}

    for day, present_list in attendance.items():
        for roll_no in present_list:
            if roll_no in counts:
                counts[roll_no] += 1

    return counts

def show_attendance_summary(students):
    counts = attendance_count_per_student(students)

    if not counts:
        print("No students registered yet.")
        return

    print("\n--- Attendance Summary (days present) ---")
    for roll_no, count in counts.items():
        name = students[roll_no]['name']
        print(f"Roll No: {roll_no} | Name: {name} | Days Present: {count}")

def show_top_attendance(students, n=1):
    counts = attendance_count_per_student(students)

    if not counts:
        print("No students registered yet.")
        return

    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    print(f"\n--- Top {n} Student(s) by Attendance ---")
    for roll_no, count in sorted_counts[:n]:
        name = students[roll_no]['name']
        print(f"Roll No: {roll_no} | Name: {name} | Days Present: {count}")

def show_kth_highest_attendance(students, k):
    counts = attendance_count_per_student(students)

    if not counts or k > len(counts) or k < 1:
        print("Invalid rank or no data available.")
        return

    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    roll_no, count = sorted_counts[k - 1]
    name = students[roll_no]['name']
    print(f"\n{k}-th highest attendance: Roll No {roll_no} | Name: {name} | Days Present: {count}")