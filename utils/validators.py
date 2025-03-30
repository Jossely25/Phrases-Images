import re

def validate_registration(name, last_name, alias, email):
    if not all([name, last_name, alias, email]):  
        return False

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))  
