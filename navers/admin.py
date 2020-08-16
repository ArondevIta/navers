from django.contrib import admin
from .models import Navers


@admin.register(Navers)
class NaversAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birthdate', 'admission_date', 'job_role', 'get_projects']
