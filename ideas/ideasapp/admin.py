from django.contrib import admin
from .models import Ideas, Vote




# Register your models here.

class InLineVotes(admin.TabularInline):
    model = Vote
@admin.register(Ideas)
class IdeasAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title', 'status']
    list_filter = ['status']
    inlines = [InLineVotes]

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'reason','idea']
    list_filter = ['idea']


