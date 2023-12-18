
from django.urls import reverse as django_reverse
from django.utils.http import urlencode



class Reverse():
    """ 
    @staticmethod
    def reverse(path, dict):
        return f"{django_reverse(path)}?{urlencode(dict)}"
     """
    @staticmethod
    def reverse(path, kwargs=None, dict=None):
        url = django_reverse(path, kwargs=kwargs)
        if dict:
            return f'{url}?{urlencode(dict)}'
        return url