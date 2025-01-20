import typing
#from typing import Dict  ## appropriate way to import a libaray

def sayHello():
    return "Hello"


def get_student_score() -> typing.Dict[str, int]:
    return {"Alice": 90, "Bob": 95, "Charlie": 92}

print(get_student_score())

from typing import Dict
def get_student_score() -> Dict[str, int]:
    return {"Alice": 90, "Bob": 95, "Charlie": 92}

print(get_student_score())