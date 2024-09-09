#validation function
def validate_int(msg:str):
    for i in msg:
        if i not in "0123456789-":
            return None
    return int(msg)

def validate_boolean(msg:str):
    if msg == "False":
        return False
    if msg == "True":
        return True
    return None

def validate_alphabet(msg:str):
    for i in msg:
        if i not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ":
            return None
    return str(msg)
