from django.contrib import admin
from .models import Hotel, HotelBooking, Contact

admin.site.register(Hotel)
admin.site.register(HotelBooking)
admin.site.register(Contact)