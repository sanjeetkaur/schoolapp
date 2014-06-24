from django.contrib import admin
from app.models import list

class schoolAdmin(admin.ModelAdmin):
    fields = ['name', 'roll_no', 'branch', 'session', 'markks', 'backlog']
admin.site.register(list)
# Register your models here.
