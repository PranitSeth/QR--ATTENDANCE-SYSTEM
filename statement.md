# Problem Statement

## Problem Statement
Manual attendance tracking in classrooms is time-consuming, error-prone, and difficult to analyze over time. Physical registers can be lost, attendance can be misrecorded, and generating attendance summaries or insights (like identifying frequently absent students) requires tedious manual counting.

## Scope of the Project
This project implements a lightweight, console-based attendance management system that:
- Digitizes student registration and record-keeping
- Uses QR codes to uniquely identify each student for quick, standardized attendance marking
- Stores attendance data in a structured, retrievable format (JSON)
- Provides basic analytics to help identify attendance patterns

The scope is limited to a single class/department-level use case, with local file-based storage (not a networked/multi-user system).

## Target Users
- College/school faculty or teaching assistants responsible for tracking student attendance
- Small institutions or individual class instructors who want a simple, low-cost digital attendance solution without needing complex, expensive attendance software

## High-Level Features
- Student registration with duplicate prevention
- Unique QR code generation per student
- Daily attendance marking and date-wise attendance viewing
- Attendance analytics: summaries, top attendees, and Kth-highest attendance lookup