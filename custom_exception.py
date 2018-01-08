class NameTooShort(ValueError):
    pass
def validate(name):
    if len(name)<10:
        raise NameTooShort(name)

validate("joe")
