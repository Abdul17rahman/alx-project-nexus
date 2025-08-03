from django.contrib import admin
from .models import Job, JobType, Location, Skill


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'job_type', 'posted_by', 'created_at')
    search_fields = ('title', 'location', 'description')
    list_filter = ('job_type', 'location')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country',)
    search_fields = ('country',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
