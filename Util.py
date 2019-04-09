from random import randrange
from datetime import timedelta
from random import choice
from string import ascii_letters


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def generate_string(size):
    """
    This function will return a random string size of size
    """
    return ''.join([choice(ascii_letters) for n in range(size)])


def generate_name_string(name, size):
    return name + generate_string(size)


def generate_person_name_string():
    names = ["Anton", "Oleg", "Irina", "Alena", "Yulia", "Svetlana", "Dmitriy", "Amalia", "John", "Victor"]
    surnames = ["Shultz", "Ruban", "Karno", "Kovalenko", "Simonenko", "Kern", "Bubenko", "Davidenko", "Krast", "Topol"]
    return names[randrange(len(names))] + surnames[randrange(len(surnames))]
