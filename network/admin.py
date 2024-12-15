from django.contrib import admin
from .models import Contacts, Network, Product


class NetworkAdmin(admin.ModelAdmin):
    """"""
    list_display = ('name', 'city', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request, 'Задолженность очищена.')


admin.site.register(Contacts)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Product)
