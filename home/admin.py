from django.contrib import admin
from home.models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_payment', 'date_expiration')
    list_filter = ('date_payment', 'date_expiration')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    ordering = ('date_expiration',)