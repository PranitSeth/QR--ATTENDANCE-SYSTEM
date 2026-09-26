# QR Attendance System

## Overview
The QR Attendance System is a console-based Python application designed to simplify and digitize student attendance tracking. It allows an administrator to register students, generate unique QR codes for each student (encoding their roll number), mark attendance, and analyze attendance data through reports — all through a simple menu-driven interface.

This project was built as part of the CSE1021 (Introduction to Problem Solving and Programming) course, applying core concepts such as functions, dictionaries, file handling, conditional logic, loops, and array/list techniques (sorting, finding maximum values, and finding the Kth largest element).

## Features
- **Student Registration** — Register students with roll number, name, and phone number; prevents duplicate roll number entries.
- **QR Code Generation** — Generate a unique QR code (encoding the roll number) for one student or all registered students at once.
- **Attendance Marking** — Mark a student present for the current date; prevents marking the same student twice in a day.
- **Attendance Viewing** — View the list of students present on any given date.
- **Reports & Analytics**:
  - View all registered students
  - View attendance summary (total days present per student)
  - View top N students by attendance
  - Find the Kth highest attendance among students

## Technologies / Tools Used
- **Language:** Python 3
- **Libraries:** `qrcode`, `Pillow` (PIL), `json`, `os`, `datetime`
- **Storage:** JSON files (`students.json`, `attendance.json`)
- **Version Control:** Git & GitHub
- **IDE:** VS Code

## Project Structure


## How to Use / Testing Instructions
1. Choose **1** to register a new student (enter roll number, name, phone).
2. Choose **2** or **3** to generate QR code(s) for registered students — saved inside the `qr_codes/` folder.
3. Choose **4** to mark attendance for a student (by roll number).
4. Choose **5** to view attendance for a specific date (or press Enter for today).
5. Choose **6–9** to view reports: all students, attendance summary, top N attendees, or Kth highest attendance.
6. Choose **10** to exit the program.