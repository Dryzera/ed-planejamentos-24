from django.contrib import admin
from teachers.models import Matter, School, Activities 

admin.site.register(Matter)
admin.site.register(School)

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')
    ordering = ('upload_date',)
    readonly_fields = ['upload_date', 'slug']