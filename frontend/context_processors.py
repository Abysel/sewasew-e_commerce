from .models import *


def catagories(request):
    return {'catagories': Category.get_all_category()}
