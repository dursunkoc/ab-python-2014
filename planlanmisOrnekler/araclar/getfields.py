#-*- encoding: utf-8 -*-

def info(object):
    """Print methods and doc strings.

    Takes module, class, list, dictionary, or string."""

    attributeList = [method for method in dir(object) if not callable(getattr(object, method)) and not method.startswith("_")]
    return attributeList
