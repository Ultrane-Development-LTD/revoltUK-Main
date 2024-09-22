from django.contrib import admin
from .models import Legislation, VotingSession, Category

class LegislationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'created_at')  # Ensure 'created_at' exists

class VotingSessionAdmin(admin.ModelAdmin):
    list_display = ('legislation', 'start_time', 'end_time', 'is_active')  # Change 'duration' to 'end_time'

admin.site.register(Category)
admin.site.register(Legislation, LegislationAdmin)
admin.site.register(VotingSession, VotingSessionAdmin)
