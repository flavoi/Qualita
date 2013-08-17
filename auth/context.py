"""
	Custom context processors for this app
"""

from datetime import date

def copyright(request):
   START_YEAR = '2013'
   this_year = date.today().year
   copy_year = START_YEAR + " - " + this_year
   return {'copyright': copy_year}