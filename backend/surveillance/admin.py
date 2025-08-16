from django.contrib import admin
from .models import Disease, District, WeeklySurveillanceData, DistrictCaseData


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'province', 'population', 'created_at']
    search_fields = ['name', 'province']
    list_filter = ['province']
    ordering = ['name']


class DistrictCaseDataInline(admin.TabularInline):
    model = DistrictCaseData
    extra = 0


@admin.register(WeeklySurveillanceData)
class WeeklySurveillanceDataAdmin(admin.ModelAdmin):
    list_display = ['week_number', 'year', 'disease', 'current_week_cases', 'change_in_cases', 'trend']
    list_filter = ['year', 'week_number', 'disease']
    search_fields = ['disease__name', 'trend']
    ordering = ['-year', '-week_number', 'disease__name']
    inlines = [DistrictCaseDataInline]


@admin.register(DistrictCaseData)
class DistrictCaseDataAdmin(admin.ModelAdmin):
    list_display = ['surveillance_data', 'district', 'cases']
    list_filter = ['district', 'surveillance_data__disease']
    search_fields = ['district__name', 'surveillance_data__disease__name']
    ordering = ['-cases']
