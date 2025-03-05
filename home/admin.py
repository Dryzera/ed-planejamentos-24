from django.contrib import admin
from home.models import Matter, School, UserProfile, Activities, PromptIa

admin.site.register(Matter)
admin.site.register(School)
admin.site.register(PromptIa)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_payment', 'date_expiration')
    list_filter = ('date_payment', 'date_expiration')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    ordering = ('date_expiration',)

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')
    ordering = ('upload_date',)
    readonly_fields = ['upload_date', 'slug']