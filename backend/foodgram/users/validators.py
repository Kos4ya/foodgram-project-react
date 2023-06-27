from django.core.exceptions import ValidationError
import re

def isValidHexaCode(value):
    regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

    p = re.compile(regex)
    if re.search(p, value):
        return True
    else:
        return False


def validate_username(value):
    if value == 'me':
        raise ValidationError(
            'Имя пользователя "me" не разрешено.'
        )
    return value
