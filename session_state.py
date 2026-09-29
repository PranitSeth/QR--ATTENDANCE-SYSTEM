import random
import string
import time

current_code = None
code_time = 0
class_label = None
CODE_LIFETIME = 45  # seconds

def new_code():
    global current_code, code_time
    current_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    code_time = time.time()
    return current_code

def is_code_valid(code):
    if current_code is None:
        return False
    if code != current_code:
        return False
    return (time.time() - code_time) <= CODE_LIFETIME
