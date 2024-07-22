from django.contrib import admin
from .models import Contact, Reservation

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','timeStamp')
    search_fields = ['name', 'email']

admin.site.register(Contact, ContactAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reg_name', 'reg_email', 'reg_phone','reg_date', 'reg_time')
    search_fields = ['reg_name', 'reg_email']

admin.site.register(Reservation, ReservationAdmin)
