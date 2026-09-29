import socket
import threading
import time
import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import session_state
from server import run_server
from excel_store import start_class

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def start_class_session(class_label):
    session_state.class_label = class_label
    start_class(class_label)

    threading.Thread(target=run_server, daemon=True).start()
    ip = get_local_ip()

    window = tk.Tk()
    window.title(f"Attendance QR - {class_label}")
    label = tk.Label(window)
    label.pack()
    info = tk.Label(window, text=f"Students must be on the same Wi-Fi as {ip}")
    info.pack()

    def refresh():
        code = session_state.new_code()
        url = f"http://{ip}:5000/mark?code={code}"
        img = qrcode.make(url).resize((300, 300))
        tk_img = ImageTk.PhotoImage(img)
        label.configure(image=tk_img)
        label.image = tk_img
        window.after(20000, refresh)

    refresh()
    window.mainloop()