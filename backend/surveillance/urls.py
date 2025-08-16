from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for ViewSets
router = DefaultRouter()
router.register(r'diseases', views.DiseaseViewSet)
router.register(r'districts', views.DistrictViewSet)
router.register(r'surveillance-data', views.WeeklySurveillanceDataViewSet)

urlpatterns = [
    # ViewSet URLs
    path('api/v1/', include(router.urls)),
    
    # Custom API endpoints
    path('api/v1/ewars/national-overview/', views.national_overview, name='national-overview'),
    path('api/v1/ewars/disease-tracker/', views.disease_tracker, name='disease-tracker'),
    path('api/v1/ewars/outbreak-alerts/', views.outbreak_alerts, name='outbreak-alerts'),
    path('api/v1/ewars/safety-tips/', views.safety_tips, name='safety-tips'),
]
