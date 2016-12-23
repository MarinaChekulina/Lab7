from django.contrib import admin
from .models import Car, Sales, Address, User1


# Register your models here.

def upper_sign(obj):
    return obj.name.upper()


class AdminModel(admin.ModelAdmin):
    list_display = ('name', 'price', 'country', 'max_speed', 'type_of_transmission', upper_sign)
    list_filter = ('country', 'price')
    search_fields = ['name']




        # def percent_win(self, obj):
    #     return '{0:.1%}'.format(obj.win / obj.games)


class PersonModel(admin.ModelAdmin):
    last_display = ('first_name', 'last_name', 'age', 'phone')
    list_filter = ['age']
    search_fields = ['first_name']



admin.site.register(Car, AdminModel)
admin.site.register(Sales)
admin.site.register(Address)
admin.site.register(User1, PersonModel)
