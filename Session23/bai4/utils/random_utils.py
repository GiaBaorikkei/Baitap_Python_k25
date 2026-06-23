import random
import string


def generate_assignment_code():

    characters = (

        string.ascii_uppercase
        + string.digits

    )

    code = "".join(

        random.choices(
            characters,
            k=4
        )

    )

    return f"PY-{code}"