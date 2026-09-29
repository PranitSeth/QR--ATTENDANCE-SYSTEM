# QR Attendance System

## Overview
A Python-based attendance system where the teacher starts a class session, showing a QR code on their laptop that refreshes every 20 seconds. Students scan it with their phone, enter their name and registration number on a simple web form, and are marked present automatically in an Excel sheet. No student ever touches the terminal.

Built for CSE1021 (Introduction to Problem Solving and Programming), applying functions, dictionaries, loops, conditionals, sorting, and file handling.

## Features
- **Student Registration** — one-time registration per student (reg no, name), stored in `attendance.xlsx`; duplicate registration numbers are rejected.
- **Student Deletion** — remove a registered student by registration number.
- **Rotating QR Attendance** — teacher starts a session; a QR code refreshing every 20 seconds is shown; each code is valid only for that window, preventing reuse of an old screenshot.
- **Self-Service Marking** — student scans the QR, submits their name and registration number on a phone web page; the system verifies the name matches the registration number before marking them present.
- **Excel-Based Records** — one row per student, one column per class session, Present/Absent, viewable directly in Excel.
- **Reports** — view all students, attendance summary (classes present per student), and top N students by attendance.

## Technologies / Tools Used
- **Language:** Python 3
- **Libraries:** `flask`, `openpyxl`, `qrcode`, `pillow`, `tkinter`
- **Storage:** Excel (`attendance.xlsx`)
- **Version Control:** Git & GitHub

## Project Structure

QR-attendance_system/
├── QR_attendance_system.py # Main menu
├── excel_store.py # Reads/writes attendance.xlsx
├── qr_session.py # Rotating QR window (tkinter)
├── server.py # Flask server, phone-facing form
├── session_state.py # Tracks current QR code and expiry
├── reports.py # Attendance summaries and rankings
├── attendance.xlsx # Student and attendance data
├── README.md
└── statement.md

https://github.com/PranitSeth/QR--ATTENDANCE-SYSTEM.gitv


## How to Use
1. Choose **1** to register each student once (reg no, name).
2. Choose **2** to start a class session; enter a label (e.g. today's date). A QR code appears, refreshing every 20 seconds.
3. Students scan the QR on their phones (same Wi-Fi as the teacher's laptop), enter their name and registration number, and submit.
4. Choose **3–5** to view students, attendance summary, or top attendees.
5. Choose **6** to delete a registered student.
6. Choose **7** to exit.

## Non-Functional Requirements
- **Performance** — attendance is marked within 1–2 seconds of submission.
- **Reliability** — duplicate registrations and duplicate attendance marks are rejected; a name/registration-number mismatch is caught before marking.
- **Usability** — students interact only through a simple phone web form; the teacher's terminal has just two steps per class.
- **Scalability** — Excel storage comfortably handles a class of 60–70 students; a database would be needed for institution-wide scale.

## Future Enhancements
- Show a live countdown on the QR window.
- Institution-wide deployment with a proper database instead of a single Excel file.