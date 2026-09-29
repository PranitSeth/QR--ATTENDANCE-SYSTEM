from flask import Flask, request
import session_state
from excel_store import get_students, mark_present

app = Flask(__name__)

PAGE_STYLE = """
<style>
  body { font-family: Arial, sans-serif; background: #f4f6f8; display: flex;
         justify-content: center; align-items: center; height: 100vh; margin: 0; }
  .card { background: white; padding: 30px 40px; border-radius: 12px;
          box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; width: 300px; }
  input[type=text] { width: 100%; padding: 10px; margin: 8px 0 16px 0;
                      border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }
  button { background: #2563eb; color: white; border: none; padding: 12px 24px;
           border-radius: 6px; font-size: 16px; cursor: pointer; width: 100%; }
  h2 { color: #111827; }
  h3 { color: #111827; }
</style>
"""

FORM_PAGE = PAGE_STYLE + """
<div class="card">
  <h2>Mark Attendance</h2>
  <form method="POST" action="/submit">
      <input type="hidden" name="code" value="{code}">
      <label>Name</label>
      <input type="text" name="name" required>
      <label>Registration Number</label>
      <input type="text" name="reg_no" required>
      <button type="submit">Submit</button>
  </form>
</div>
"""

def message_page(text):
    return PAGE_STYLE + f'<div class="card"><h3>{text}</h3></div>'

@app.route("/mark")
def mark_page():
    code = request.args.get("code", "")
    if not session_state.is_code_valid(code):
        return message_page("This QR has expired. Ask your teacher for the current one.")
    return FORM_PAGE.replace("{code}", code)

@app.route("/submit", methods=["POST"])
def submit():
    code = request.form.get("code", "")
    name_entered = request.form.get("name", "").strip()
    reg_no = request.form.get("reg_no", "").strip()

    if not session_state.is_code_valid(code):
        return message_page("This QR has expired. Ask your teacher for the current one.")

    students = get_students()
    reg_key = reg_no.upper()
    if reg_key not in students:
        return message_page("Registration number not found. Check and try again.")

    actual_name = students[reg_key]
    if name_entered.lower() != str(actual_name).strip().lower():
        return message_page(f"Name does not match our records for {reg_no}. Check and try again.")

    result = mark_present(reg_no, session_state.class_label)
    if result == "marked":
        return message_page(f"Attendance marked for {actual_name}. You're done.")
    elif result == "already":
        return message_page(f"{actual_name} is already marked present.")
    else:
        return message_page(f"Could not mark attendance ({result}). Tell your teacher.")

def run_server():
    app.run(host="0.0.0.0", port=5000) 