from django.contrib import admin
from reservas.models import Table, Reservation

class TablesAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')
    list_editable = ('capacity',)
    search_fields = ('number',)
    list_filter = ('capacity',)
    list_per_page = 20
    ordering = ('number',)
admin.site.register(Table, TablesAdmin)


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('table', 'client', 'reservation_date', 'reservation_time')
    search_fields = ('client', 'table')
    list_filter = ('table', 'reservation_date')
admin.site.register(Reservation, ReservationsAdmin)
