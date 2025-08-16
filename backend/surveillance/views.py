from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Count, Q, Max
from .models import Disease, District, WeeklySurveillanceData, DistrictCaseData
from .serializers import (
    DiseaseSerializer, DistrictSerializer, WeeklySurveillanceDataSerializer,
    DiseaseTrackerSerializer, NationalOverviewSerializer
)


class DiseaseViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for Disease model"""
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for District model"""
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class WeeklySurveillanceDataViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for WeeklySurveillanceData model"""
    queryset = WeeklySurveillanceData.objects.select_related('disease').prefetch_related('district_cases__district')
    serializer_class = WeeklySurveillanceDataSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by disease
        disease = self.request.query_params.get('disease')
        if disease:
            queryset = queryset.filter(disease__name__icontains=disease)
        
        # Filter by week
        week = self.request.query_params.get('week')
        if week:
            queryset = queryset.filter(week_number=week)
        
        # Filter by year
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(year=year)
            
        return queryset.order_by('-week_number', 'disease__name')


@api_view(['GET'])
def national_overview(request):
    """API endpoint for national health overview"""
    try:
        # Get latest week data
        latest_week = WeeklySurveillanceData.objects.aggregate(
            max_week=Max('week_number')
        )['max_week']
        
        if not latest_week:
            return Response({
                'error': 'No surveillance data available'
            }, status=status.HTTP_404_NOT_FOUND)
        
        latest_data = WeeklySurveillanceData.objects.filter(
            week_number=latest_week
        ).select_related('disease')
        
        # Calculate statistics
        total_cases = latest_data.aggregate(
            total=Sum('current_week_cases')
        )['total'] or 0
        
        active_diseases = latest_data.filter(
            current_week_cases__gt=0
        ).count()
        
        trending_up = latest_data.filter(
            Q(trend__icontains='increase') | Q(trend__icontains='increasing')
        ).count()
        
        trending_down = latest_data.filter(
            Q(trend__icontains='decrease') | Q(trend__icontains='decreasing')
        ).count()
        
        # Get most affected districts
        most_affected = DistrictCaseData.objects.filter(
            surveillance_data__week_number=latest_week
        ).values('district__name').annotate(
            total_cases=Sum('cases')
        ).order_by('-total_cases')[:5]
        
        most_affected_districts = [
            {'name': item['district__name'], 'cases': item['total_cases']}
            for item in most_affected
        ]
        
        # Get recent outbreaks (diseases with significant increases)
        recent_outbreaks = latest_data.filter(
            Q(change_in_cases__gt=10) | Q(trend__icontains='large increase')
        ).order_by('-change_in_cases')[:5]
        
        response_data = {
            'total_cases': total_cases,
            'active_diseases': active_diseases,
            'trending_up': trending_up,
            'trending_down': trending_down,
            'most_affected_districts': most_affected_districts,
            'recent_outbreaks': WeeklySurveillanceDataSerializer(recent_outbreaks, many=True).data,
            'latest_week': latest_week
        }
        
        return Response(response_data)
        
    except Exception as e:
        return Response({
            'error': f'Error generating national overview: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def disease_tracker(request):
    """API endpoint for disease tracking dashboard"""
    try:
        # Get latest week data
        latest_week = WeeklySurveillanceData.objects.aggregate(
            max_week=Max('week_number')
        )['max_week']
        
        if not latest_week:
            return Response({
                'error': 'No surveillance data available'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Get disease data for latest week
        disease_data = WeeklySurveillanceData.objects.filter(
            week_number=latest_week
        ).select_related('disease').order_by('-current_week_cases')
        
        serializer = DiseaseTrackerSerializer(disease_data, many=True)
        
        return Response({
            'week_number': latest_week,
            'diseases': serializer.data
        })
        
    except Exception as e:
        return Response({
            'error': f'Error generating disease tracker data: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def outbreak_alerts(request):
    """API endpoint for outbreak alerts"""
    try:
        # Get latest week data
        latest_week = WeeklySurveillanceData.objects.aggregate(
            max_week=Max('week_number')
        )['max_week']
        
        if not latest_week:
            return Response({
                'error': 'No surveillance data available'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Get alerts based on significant increases or concerning trends
        alerts = WeeklySurveillanceData.objects.filter(
            week_number=latest_week
        ).filter(
            Q(change_in_cases__gt=20) |
            Q(trend__icontains='large increase') |
            Q(trend__icontains='significantly increasing') |
            Q(current_week_cases__gt=100)
        ).select_related('disease').order_by('-change_in_cases')
        
        alert_data = []
        for alert in alerts:
            severity = 'high' if alert.change_in_cases and alert.change_in_cases > 50 else 'medium'
            if alert.current_week_cases and alert.current_week_cases > 200:
                severity = 'high'
            
            alert_data.append({
                'id': alert.id,
                'disease': alert.disease.name,
                'current_cases': alert.current_week_cases,
                'change': alert.change_in_cases,
                'trend': alert.trend,
                'affected_areas': alert.top_affected_districts,
                'severity': severity,
                'week': alert.week_number
            })
        
        return Response({
            'alerts': alert_data,
            'total_alerts': len(alert_data)
        })
        
    except Exception as e:
        return Response({
            'error': f'Error generating outbreak alerts: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def safety_tips(request):
    """API endpoint for safety tips based on current outbreaks"""
    try:
        # Get latest week data
        latest_week = WeeklySurveillanceData.objects.aggregate(
            max_week=Max('week_number')
        )['max_week']
        
        if not latest_week:
            return Response({
                'error': 'No surveillance data available'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Get active diseases
        active_diseases = WeeklySurveillanceData.objects.filter(
            week_number=latest_week,
            current_week_cases__gt=0
        ).select_related('disease').order_by('-current_week_cases')
        
        # Generate safety tips based on active diseases
        safety_tips = []
        
        disease_tips = {
            'Dengue': [
                'Remove stagnant water around your home',
                'Use mosquito nets while sleeping',
                'Wear long-sleeved clothing during dawn and dusk',
                'Seek medical attention for high fever'
            ],
            'Malaria': [
                'Use insecticide-treated bed nets',
                'Apply mosquito repellent',
                'Keep surroundings clean and dry',
                'Seek immediate medical care for fever and chills'
            ],
            'Cholera': [
                'Drink only boiled or bottled water',
                'Eat thoroughly cooked food',
                'Wash hands frequently with soap',
                'Avoid street food and raw vegetables'
            ],
            'SARI': [
                'Wear masks in crowded places',
                'Maintain social distancing',
                'Wash hands frequently',
                'Seek medical attention for breathing difficulties'
            ],
            'AGE': [
                'Maintain proper hygiene',
                'Drink clean water',
                'Eat fresh, properly cooked food',
                'Seek medical care for persistent diarrhea'
            ]
        }
        
        for disease_data in active_diseases[:5]:  # Top 5 active diseases
            disease_name = disease_data.disease.name
            tips = disease_tips.get(disease_name, [
                'Maintain good hygiene practices',
                'Seek medical attention if symptoms persist',
                'Follow local health guidelines'
            ])
            
            safety_tips.append({
                'disease': disease_name,
                'current_cases': disease_data.current_week_cases,
                'priority': 'high' if disease_data.current_week_cases > 100 else 'medium',
                'tips': tips
            })
        
        return Response({
            'safety_tips': safety_tips,
            'general_tips': [
                'Maintain good personal hygiene',
                'Drink clean, boiled water',
                'Eat fresh, properly cooked food',
                'Keep your surroundings clean',
                'Seek medical attention for any unusual symptoms'
            ]
        })
        
    except Exception as e:
        return Response({
            'error': f'Error generating safety tips: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
