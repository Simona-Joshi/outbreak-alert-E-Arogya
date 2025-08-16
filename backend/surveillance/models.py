from django.db import models
from django.utils import timezone


class Disease(models.Model):
    """Model to store disease information"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class District(models.Model):
    """Model to store district information"""
    name = models.CharField(max_length=100, unique=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class WeeklySurveillanceData(models.Model):
    """Model to store weekly disease surveillance data from EWARS"""
    source_file = models.CharField(max_length=100)
    week_number = models.IntegerField()
    year = models.IntegerField(default=2024)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='surveillance_data')
    
    # Case numbers
    previous_week_cases = models.IntegerField(null=True, blank=True)
    current_week_cases = models.IntegerField(null=True, blank=True)
    change_in_cases = models.IntegerField(null=True, blank=True)
    same_week_last_year = models.IntegerField(null=True, blank=True)
    year_over_year_change = models.IntegerField(null=True, blank=True)
    
    # Trend analysis
    trend = models.CharField(max_length=200, blank=True, null=True)
    
    # Geographic data
    top_affected_districts = models.TextField(blank=True, null=True)  # Store as JSON or comma-separated
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Week {self.week_number} - {self.disease.name} ({self.current_week_cases} cases)"

    class Meta:
        ordering = ['-week_number', 'disease__name']
        unique_together = ['week_number', 'year', 'disease']


class DistrictCaseData(models.Model):
    """Model to store district-specific case data"""
    surveillance_data = models.ForeignKey(WeeklySurveillanceData, on_delete=models.CASCADE, related_name='district_cases')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='case_data')
    cases = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.district.name}: {self.cases} cases"

    class Meta:
        ordering = ['-cases']
        unique_together = ['surveillance_data', 'district']
