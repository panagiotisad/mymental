# used to register database models to admin page
from django.contrib import admin

from .models import Rating_data, To_do_list

admin.site.register(Rating_data)
admin.site.register(To_do_list)
