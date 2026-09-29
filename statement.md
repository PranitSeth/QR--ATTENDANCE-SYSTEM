# Problem Statement

## Problem Statement
Manual and Excel-based attendance tracking is slow, error-prone, and gives teachers no way to prevent proxy attendance, since anyone can mark a name present on a paper register or a shared sheet without the actual student being present.

## Scope of the Project
This project implements a QR-based attendance system where the teacher starts a class session showing a QR code that refreshes every 20 seconds. Students scan it and submit their name and registration number themselves, from their own phone, which is checked against registered records before being marked present. All data is stored in an Excel file, one row per student and one column per class.

The scope is limited to a single class or department-level use case, with local, offline storage rather than a networked, multi-user system.

## Target Users
- College or school faculty who currently take attendance manually or through a plain Excel/paper register
- Small institutions or individual instructors who want a fast, low-cost, self-service attendance system without buying dedicated attendance software

## High-Level Features
- One-time student registration (registration number, name)
- Teacher-started class sessions with a rotating, time-limited QR code
- Student self-service attendance marking through a phone web form, with name verification
- Excel-based attendance records, viewable directly without extra tools
- Attendance summaries and top-attendee rankings