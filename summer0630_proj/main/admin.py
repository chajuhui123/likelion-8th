from django.contrib import admin
from .models import Orders, Members, Goods, Sheets

# Register your models here.
admin.site.register(Orders)
admin.site.register(Members)
admin.site.register(Goods)
admin.site.register(Sheets)
