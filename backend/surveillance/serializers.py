from rest_framework import serializers
from .models import Disease, District, WeeklySurveillanceData, DistrictCaseData


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'province', 'population', 'created_at', 'updated_at']


class DistrictCaseDataSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    
    class Meta:
        model = DistrictCaseData
        fields = ['id', 'district', 'cases']


class WeeklySurveillanceDataSerializer(serializers.ModelSerializer):
    disease = DiseaseSerializer(read_only=True)
    district_cases = DistrictCaseDataSerializer(many=True, read_only=True)
    
    class Meta:
        model = WeeklySurveillanceData
        fields = [
            'id', 'source_file', 'week_number', 'year', 'disease',
            'previous_week_cases', 'current_week_cases', 'change_in_cases',
            'same_week_last_year', 'year_over_year_change', 'trend',
            'top_affected_districts', 'district_cases', 'created_at', 'updated_at'
        ]


class DiseaseTrackerSerializer(serializers.ModelSerializer):
    """Simplified serializer for disease tracking dashboard"""
    disease_name = serializers.CharField(source='disease.name')
    
    class Meta:
        model = WeeklySurveillanceData
        fields = [
            'week_number', 'disease_name', 'current_week_cases',
            'change_in_cases', 'trend', 'top_affected_districts'
        ]


class NationalOverviewSerializer(serializers.Serializer):
    """Serializer for national health overview"""
    total_cases = serializers.IntegerField()
    active_diseases = serializers.IntegerField()
    trending_up = serializers.IntegerField()
    trending_down = serializers.IntegerField()
    most_affected_districts = serializers.ListField()
    recent_outbreaks = WeeklySurveillanceDataSerializer(many=True)
