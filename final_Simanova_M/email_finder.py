import re
from typing import List

def find_emails(text: str) -> List[str]:

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text, re.IGNORECASE)
    return emails