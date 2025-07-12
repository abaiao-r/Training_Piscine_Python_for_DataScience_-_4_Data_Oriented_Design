import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random 15-letter lowercase ID.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Data class representing a student.

    Fields:
        - name: Student's first name
        - surname: Student's last name
        - active: Set to True by default
        - login: Auto-generated, first letter of name + surname (capitalized)
        - id: Auto-generated 15-character lowercase string
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """
        Post-initialization to compute login and generate ID.
        """
        # Make login: first letter of name + surname (capitalized)
        self.login = f"{self.name[0]}{self.surname}".capitalize()
        self.id = generate_id()
