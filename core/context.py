"""
	Custom context processors for the core app.
"""

from datetime import date
from models import Interrogazione

"""
    Automatic copyright to the current year.
"""
def copyright(request):
    START_YEAR = 2013
    this_year = date.today().year
    if START_YEAR != this_year:
        copy_year = "%s - %s" % (START_YEAR, this_year)
    else:
    	copy_year = START_YEAR
    return {'copyright': copy_year}

"""
    Interrogazione objects are critical in many templates.
"""
def interrogazioni(request):
	interrogazioni = Interrogazione.objects.all().values()
	return {'interrogazioni': interrogazioni}