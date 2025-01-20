#import typing
from typing import Optional

def display_message(mesage: Optional[str] = None) -> str:
    if mesage:
        return f"Message: {mesage}"
    else:
        return "No mesage provided"

print()
print()
print(display_message("Hope you enjoy Week 03!"))
print(" ================================= ")
print(display_message())