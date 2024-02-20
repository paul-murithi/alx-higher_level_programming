#!/usr/bin/python3
""" Python - Inheritance """


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    otherwise False.
    Args:
        obj: The object
        a_class (Class): The class to compare to
    """
    if type(obj) == a_class:
        return (False)
    return (issubclass(type(obj), a_class))
