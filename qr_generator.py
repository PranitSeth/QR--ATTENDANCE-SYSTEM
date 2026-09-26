import qrcode
import os

QR_FOLDER = "qr_codes"

def generate_qr_for_student(roll_no, students):
    if roll_no not in students:
        print("No such student found. Please register first.")
        return

    if not os.path.exists(QR_FOLDER):
        os.makedirs(QR_FOLDER)

    name = students[roll_no]["name"]
    data = f"{roll_no}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    file_path = os.path.join(QR_FOLDER, f"{roll_no}.png")
    img.save(file_path)

    print(f"QR code generated for {name} (Roll No: {roll_no}) -> {file_path}")

def generate_qr_for_all(students):
    if not students:
        print("No students registered yet.")
        return

    if not os.path.exists(QR_FOLDER):
        os.makedirs(QR_FOLDER)

    for roll_no in students:
        generate_qr_for_student(roll_no, students)

    print(f"\nGenerated QR codes for {len(students)} student(s).")